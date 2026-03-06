# -*- mode: python ; coding: utf-8 -*-
# YO Log PRO v17 — PyInstaller spec file
# Python 3.8.10 — Windows 7/8/10/11 compatible
# Build: pyinstaller YO_Log_PRO_v17.spec

block_cipher = None

a = Analysis(
    ['yo_log_pro.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('contests.json', '.'),
        ('config.json', '.'),
        ('icon.ico', '.'),
    ],
    hiddenimports=[
        'serial',
        'serial.tools',
        'serial.tools.list_ports',
        'tkinter',
        'tkinter.ttk',
        'tkinter.messagebox',
        'tkinter.filedialog',
        'tkinter.scrolledtext',
        'tkinter.colorchooser',
        'threading',
        'socket',
        'json',
        'csv',
        'hashlib',
        'pathlib',
        'collections',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'numpy', 'pandas', 'matplotlib', 'scipy',
        'PIL', 'PyQt5', 'wx', 'gi',
        'IPython', 'jupyter',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='YO_Log_PRO_v17',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',
    version_file=None,
)
