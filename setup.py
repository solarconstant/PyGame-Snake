import cx_Freeze

executables = [cx_Freeze.Executable('Intro.py')]

cx_Freeze.setup(
	name = 'Snake',
	options = {'build_exe':{'packages': ['pygame'], 'include_files':['head.png', 'samosa.png']}},
	description = 'Snake game',
	executables = executables
	)