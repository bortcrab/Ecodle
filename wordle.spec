# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['wordle.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\english_words\\data\\web2_lower.pickle', 'english_words\\data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='wordle',
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
    icon=['wordleLogo.ico'],
)
