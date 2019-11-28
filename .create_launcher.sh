#!/bin/sh

APPDIR="$( cd "$(dirname "$0")" ; pwd -P )"
PYTHON_BIN=$APPDIR/venv/bin/python3
PYTHON_MAIN=$APPDIR/main.py
EXEC_COMMAND="$PYTHON_BIN $PYTHON_MAIN"

create_launcher () {
	app_dir=$1
	launcher_file=$2
	icon_file=$3
	launcher_name=$4
	exec_command=$5
	run_in_terminal=$6
	
	printf "#!/usr/bin/env xdg-open
[Desktop Entry]
Version=1.0
Type=Application
Terminal=$run_in_terminal
Exec=$exec_command
Name[en_US]=$launcher_name
Comment[en_US]=$launcher_name
Icon[en_US]=$icon_file
Name=$launcher_name
Comment=$launcher_name
Icon=$icon_file
Path=$app_dir
" | tee  "$launcher_file" > /dev/null

	chmod +x "$launcher_file"
	echo "-------------------------------------------"
	echo "INFO ABOUT CREATED FILE:"
	echo "-> Icon File: \"$icon_file\""
	echo "-> Exec Command of Launcher: \"$exec_command\""
	echo "-> Launcher Name: \"$launcher_name\""
	echo "-> Created Launcher File: \"$launcher_file\""
	echo "-------------------------------------------"
}

main(){
	launcher_file="$APPDIR/RunKafkaServer.desktop"
	icon_file="$APPDIR/.icon.png"
	launcher_name="Run"
	exec_command=$EXEC_COMMAND
	run_in_terminal=false
	create_launcher "$APPDIR" "$launcher_file" "$icon_file" "$launcher_name" "$EXEC_COMMAND" $run_in_terminal
}

main



