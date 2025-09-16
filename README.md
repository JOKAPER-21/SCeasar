Production Pipeline For Small Project


assets :
    blender or other files for presets

build :
    Final addons

docs :
    About scripts

src :
    softwares addons and project lancher

How to use SCeasar Addon

Method: 01
    * Step 01: Copy **"SCeasar\src\blender\script"** from github.
    * Step 02: Paste it to **"C:\Users\<user name>\AppData\Roaming\Blender Foundation\Blender\4.5\scripts\addons\SCeasar"**.
    * Step 03: Open blender Edit >  Preferences > Add-ons > Enable SCeaser.
    * Step 04: Check in N-Panel in 3d_View.

Method: 02
    * Step 01: Download **"https://github.com/JOKAPER-21/SCeasar"** to local.
    * Step 02: Open folder called **SCeasar\src\blender**
    * Step 03: Open file **update_tools.py** in notepad.
    * Step 04: Replace src = r"<root folder>\SCeasar\src\blender\script".
    * Step 05: Replace dst = r"C:\Users\<user name>\AppData\Roaming\Blender Foundation\Blender\4.5\scripts\addons\SCeasar".
    * Step 06: To open blender double click **update_tools.py**. (NOTE: Run scrip for the first and only for updates.)
