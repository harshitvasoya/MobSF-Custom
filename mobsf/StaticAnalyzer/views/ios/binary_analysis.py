# -*- coding: utf_8 -*-
"""Module for iOS IPA Binary Analysis."""

import logging
from pathlib import Path


from macholib.mach_o import (CPU_TYPE_NAMES, MH_CIGAM_64, MH_MAGIC_64,
                             get_cpu_subtype)
from macholib.MachO import MachO

from mobsf.StaticAnalyzer.views.ios.classdump import (
    get_class_dump,
)
from mobsf.StaticAnalyzer.views.common.binary.lib_analysis import (
    MachOChecksec,
)
from mobsf.StaticAnalyzer.views.common.binary.strings import (
    strings_on_binary,
)
from mobsf.StaticAnalyzer.views.ios.binary_rule_matcher import (
    binary_rule_matcher,
)
from mobsf.MobSF.utils import (
    append_scan_status,
)

logger = logging.getLogger(__name__)


def detect_bin_type(libs):
    """Detect IPA binary type."""
    if any('libswiftCore.dylib' in itm for itm in libs):
        return 'Swift'
    else:
        return 'Objective C'


def get_bin_info(bin_file):
    """Get Binary Information."""
    logger.info('Getting Binary Information')
    m = MachO(bin_file.as_posix())
    for header in m.headers:
        if header.MH_MAGIC == MH_MAGIC_64 or header.MH_MAGIC == MH_CIGAM_64:
            sz = '64-bit'
        else:
            sz = '32-bit'
        arch = CPU_TYPE_NAMES.get(
            header.header.cputype, header.header.cputype)
        subarch = get_cpu_subtype(
            header.header.cputype, header.header.cpusubtype)
        return {'endian': header.endian,
                'bit': sz,
                'arch': arch,
                'subarch': subarch}


def ipa_macho_analysis(binary):
    data = {
        'checksec': {},
        'symbols': [],
        'libraries': [],
    }
    try:
        logger.info('Running MachO Analysis on: %s', binary.name)
        cs = MachOChecksec(binary)
        chksec = cs.checksec()
        symbols = cs.get_symbols()
        libs = cs.get_libraries()
        data['checksec'] = chksec
        data['symbols'] = symbols
        data['libraries'] = libs
    except Exception:
        logger.exception('Running MachO Analysis')
    return data


def binary_analysis(checksum, src, tools_dir, app_dir, executable_name):
    """Binary Analysis of IPA."""
    bin_dict = {
        'checksec': {},
        'libraries': [],
        'bin_code_analysis': {},
        'strings': [],
        'bin_info': {},
        'bin_type': '',
        'bin_path': None,
    }
    try:
        binary_findings = {}
        msg = 'Starting Binary Analysis'
        logger.info(msg)
        append_scan_status(checksum, msg)

        dot_app_path = next(Path(src).glob('**/*.app'), None)

        if not dot_app_path:
            logger.warning('Could not find .app directory.')
            return bin_dict

        bin_dir = dot_app_path

        if not executable_name:
            bin_name = dot_app_path.stem
        else:
            _bin = bin_dir / executable_name
            if _bin.exists():
                bin_name = executable_name
            else:
                bin_name = dot_app_path.stem

        bin_path = bin_dir / bin_name
        
        if not (bin_path.exists() and bin_path.is_file()):
            msg = (
                f'MobSF Cannot find binary in {bin_path.as_posix()}. '
                'Skipping Binary Analysis.')
            logger.warning(msg)
            append_scan_status(checksum, 'Skipping binary analysis', msg)
        else:
            macho = ipa_macho_analysis(bin_path)
            bin_info = get_bin_info(bin_path)
            bin_type = detect_bin_type(macho['libraries'])
            classdump = get_class_dump(
                checksum,
                tools_dir,
                bin_path,
                app_dir,
                bin_type)
            binary_rule_matcher(
                checksum,
                binary_findings,
                macho['symbols'], classdump)
            bin_dict['checksec'] = macho['checksec']
            bin_dict['libraries'] = macho['libraries']
            bin_dict['bin_code_analysis'] = binary_findings
            bin_dict['bin_info'] = bin_info
            bin_dict['bin_type'] = bin_type
            logger.info('Running strings against the Binary')
            bin_dict['strings'] = strings_on_binary(bin_path.as_posix())
            bin_dict['bin_path'] = bin_path
    except Exception as exp:
        msg = 'Failed to run IPA Binary Analysis'
        logger.exception(msg)
        append_scan_status(checksum, msg, repr(exp))
    return bin_dict
