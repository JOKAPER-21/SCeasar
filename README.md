# Production Pipeline for Small Project (Beta version)

## Project Structure
- **assets** : Blender or other files for presets  
- **build** : Final addons  
- **docs** : About scripts  
- **src** : Software addons and project launcher  

---

# How to Use SCeasar Addon

## **Method 01**
1. **Download**: [SCeasar](https://github.com/JOKAPER-21/SCeasar/tree/main/src/blender/script)
2. **Paste**:  
   ```python
   `C:\Users\<user name>\AppData\Roaming\Blender Foundation\Blender\4.5\scripts\addons\SCeasar`  
   ```
3. **Enable Addon**:  
   Open **Blender** → **Edit > Preferences > Add-ons > Enable SCeasar**.  
4. **Check**: In **N-Panel** inside the 3D View.  

---

## **Method 02**
1. **Download**: [SCeasar Repository](https://github.com/JOKAPER-21/SCeasar).  
2. **Navigate**: Open folder `<donwnload SCeasar\src\blender`.  
3. **Edit File**: Open **update_tools.py** in Notepad.  
4. **Set Source Path**:  
   ```python
    src = r"<root folder>\SCeasar\src\blender\script"
    ```
    ```python
    dst = r"C:\Users\<user name>\AppData\Roaming\Blender Foundation\Blender\4.5\scripts\addons\SCeasar"
    ```