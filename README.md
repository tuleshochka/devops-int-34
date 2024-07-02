# Ansible
В файле env.yaml необходимо указать IP-адрес хоста, пользователя для ansible и пароль к нему. <br>
Предварительно на хосте должен быть установлен **openssh-server** и в файле /etc/sudoers должна быть строчка:
```
ansible ALL=(ALL:ALL) NOPASSWD:ALL
```
Для запуска плейбука использовать команду:
```
ansible-playbook playbook.yaml -e @env.yaml
```
После выполнения плейбука можно подключиться к postgresql командой:
```
psql -U postgres -h <host_ip> -p 5432
```
используя пароль из файла env.yaml