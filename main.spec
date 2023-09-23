# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py',
    'D:\\GitHub\\python-game\\openspiel\\algorithms\\mcts.py',
    'D:\\GitHub\\python-game\\openspiel\\bots\\human.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Game.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Go.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Havannah.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Hex.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Tictactoe.py',
    'D:\\GitHub\\python-game\\openspiel\\game\\Y.py',
    'D:\\GitHub\\python-game\\speechrecognition\\microphone_recognition.py',
    'D:\\GitHub\\python-game\\freegames_extern\\paint.py',
    'D:\\GitHub\\python-game\\freegames_extern\\snake.py'],
    pathex=['D:\\GitHub\\python-game'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
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
    name='main',
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
)
