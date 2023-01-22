#!/bin/bash

command1="yc compute instance list > vm_info"
command2="python3 info2sheet.py"
echo "Сбор информации о ВМ"
eval $command1
echo "Информация записана в файл vm_info и передана скрипту info2sheet.py"
eval $command2 2> /dev/null
echo "Информация о ВМ записана в таблицу!"
