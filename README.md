# 📱 Mobile Security Framework (MobSF) - Setup & Usage Guide for Windows

MobSF is an open-source mobile application (Android/iOS/Windows) automated pen-testing framework capable of static, dynamic, and malware analysis.

---
<img width="970" height="109" alt="image" src="https://github.com/user-attachments/assets/971182e9-736b-4be7-8528-29b6b02e28f1" />

## ✅ Requirements for Windows Setup

> Please ensure you install all the following dependencies **before** proceeding with MobSF installation.

### 🧰 System Prerequisites

| Tool/Package | Version | Download Link |
| :--- | :--- | :--- |
| **Git** | Latest | [Download Git](https://git-scm.com/download/win) |
| **Python** | 3.8 - 3.11 | [Download Python](https://www.python.org/) |
| **JDK (Java Development Kit)** | 11 or higher | [Download JDK](https://www.oracle.com/java/technologies/downloads/) |
| **Microsoft Visual C++ Build Tools** | Latest | [Download Build Tools](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2022) |
| **OpenSSL (non-light version)** | Latest | [Download OpenSSL](https://slproweb.com/products/Win32OpenSSL.html) |
| **wkhtmltopdf** | Latest | [Download wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) |

> **Important:** After installing `wkhtmltopdf`, **add its installation directory (e.g., `C:\Program Files\wkhtmltopdf\bin`) to your system's `PATH` environment variable.**

---

## ⚙️ Poetry Environment Variable (Optional but Recommended)

MobSF uses `poetry` for managing dependencies. To ensure it can be run from any terminal, you should add its installation location to your system's PATH.

### ➤ Step-by-Step Instructions:

1.  **Install Poetry**:
    ```powershell
    pip install poetry
    ```

2.  **Find Poetry's Installation Path**:
    Open a new Command Prompt or PowerShell and find where `poetry` was installed.
    ```powershell
    where poetry
    ```
    This will output a path, typically `C:\Users\<YourUsername>\AppData\Roaming\Python\Python3X\Scripts\poetry.exe`.

3.  **Add the Path to Environment Variables**:
    * Copy the **directory** from the previous step (e.g., `C:\Users\<YourUsername>\AppData\Roaming\Python\Python3X\Scripts`).
    * Search for "Edit the system environment variables" in the Windows Start Menu and open it.
    * Click the `Environment Variables...` button.
    * In the "User variables" section, select the `Path` variable and click `Edit...`.
    * Click `New` and paste the directory path you copied.
    * Click `OK` on all windows to save the changes. You may need to restart your terminal for the changes to take effect.

---

## 🧪 Dynamic Analysis Setup (Optional)

⚠️ **Note**: For reliable results, dynamic analysis should be performed on a physical device or a high-performance emulator setup. Performance on standard virtual machines (VMs) may vary.

You will need an Android Emulator such as:
* **Genymotion** Desktop or Cloud
* **Android Studio Emulator**

---

## 🛠️ Installing MobSF on Windows

Follow the steps below to clone and set up MobSF on your system.

1.  **Clone the MobSF repository**:
    ```powershell
    git clone https://github.com/harshitvasoya/MobSF-Custom.git
    ```

2.  **Change into the project directory**:
    ```powershell
    cd MobSF-Custom
    ```

  
3.  **Run the setup script**:
    This script will install all the required Python dependencies.
    ```powershell
    setup.bat
    ```
      <img width="1050" height="393" alt="image" src="https://github.com/user-attachments/assets/9859be47-2817-4602-a0c6-6ee1e18a1a18" />

> ⚠️ **Important Tip**: Before running `setup.bat`, ensure no other programs (like VSCode) or terminals have the MobSF directory open. File locks can cause permission errors during setup.

---

## ▶️ Running MobSF

To start the MobSF server, execute the following command from within the `Mobile-Security-Framework-MobSF` directory:

```powershell
run.bat
Once MobSF is running, open your web browser and navigate to: http://127.0.0.1:8000
```
---
## 🔬 Pen Testing with MobSF
* You can now upload .apk, .ipa, or .appx files to the MobSF web interface to begin your analysis, which includes:

* ** Static Analysis: Decompiling the app and analyzing its source code, resources, and configurations for vulnerabilities.

* ** Dynamic Analysis: Running the app in an emulated environment to monitor its behavior, network traffic, and interactions.

* ** Malware Detection: Checking for signatures of known malware families.

* ** Web API Fuzzing: Testing the app's backend APIs for common security flaws.

* For advanced usage, refer to the official documentation:
🔗 MobSF Documentation

## 📄 Notes
* ** Python Version: Always use a compatible version of Python (3.8-3.11).

* ** Updates: MobSF is under active development. Periodically run git pull in the MobSF directory to get the latest updates.

* ** Stopping the Server: Press Ctrl + C in the terminal where MobSF is running to stop the server.

## 🙌 Credits
MobSF is developed and maintained by the MobSF Team.

## 📌 License
MobSF is distributed under the GNU General Public License v3.0.

---






