Last login: Tue Jan 21 20:48:44 on console
~ ❯❯❯ ssh pi@raspberrypi.local

pi@raspberrypi.local's password: 
Linux raspberrypi 4.19.80-v7+ #1 SMP Thu Oct 31 13:37:52 JST 2019 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan  4 14:49:06 2020 from fe80::18a1:7fec:c315:22fc%eth0
pi@raspberrypi:~ $ sudo po
pod2html    pod2text    podchecker  point-rpi   poweroff    
pod2man     pod2usage   podselect   popd        
pi@raspberrypi:~ $ sudo poweroff 
Connection to raspberrypi.local closed by remote host.
Connection to raspberrypi.local closed.
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

ssh: connect to host 192.168.2.2 port 22: Connection refused
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

ssh: connect to host 192.168.2.2 port 22: Connection refused
~ ❯❯❯ cd ~/.ssh                                                          ✘ 255 
~/.ssh ❯❯❯ ls
known_hosts
~/.ssh ❯❯❯ sudo vim known_hosts
Password:
~/.ssh ❯❯❯ sudo vim known_hosts
~/.ssh ❯❯❯ cd
~ ❯❯❯ ssh ubuntu@192.168.2.2

The authenticity of host '192.168.2.2 (192.168.2.2)' can't be established.
ECDSA key fingerprint is SHA256:lxa3M48Fw/NuklhtdmG4xdvweSYlV7JJ76hvu23OmCk.
Are you sure you want to continue connecting (yes/no)? uy
Please type 'yes' or 'no': yes
Warning: Permanently added '192.168.2.2' (ECDSA) to the list of known hosts.
ubuntu@192.168.2.2's password: 
You are required to change your password immediately (root enforced)
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1041-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 16:01:57 UTC 2018

  System load:  0.07              Processes:           114
  Usage of /:   4.4% of 28.81GB   Users logged in:     0
  Memory usage: 12%               IP address for eth0: 192.168.2.2
  Swap usage:   0%

0 packages can be updated.
0 updates are security updates.



The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

WARNING: Your password has expired.
You must change your password now and login again!
Changing password for ubuntu.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
Password unchanged
Enter new UNIX password: 
Retype new UNIX password: 
Sorry, passwords do not match
passwd: Authentication token manipulation error
passwd: password unchanged
Connection to 192.168.2.2 closed.
~ ❯❯❯ ssh ubuntu@192.168.2.2                                              ✘ 10 

ubuntu@192.168.2.2's password: 
You are required to change your password immediately (root enforced)
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1041-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 16:02:42 UTC 2018

  System load:  0.6               Processes:           114
  Usage of /:   4.6% of 28.81GB   Users logged in:     0
  Memory usage: 12%               IP address for eth0: 192.168.2.2
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jan 28 16:02:04 2018 from 192.168.2.1
WARNING: Your password has expired.
You must change your password now and login again!
Changing password for ubuntu.
(current) UNIX password: 
passwd: Authentication token manipulation error
passwd: password unchanged
Connection to 192.168.2.2 closed.
~ ❯❯❯ ssh ubuntu@192.168.2.2                                              ✘ 10 

ubuntu@192.168.2.2's password: 
You are required to change your password immediately (root enforced)
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1041-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 16:03:02 UTC 2018

  System load:  0.49              Processes:           114
  Usage of /:   4.6% of 28.81GB   Users logged in:     0
  Memory usage: 12%               IP address for eth0: 192.168.2.2
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jan 28 16:02:48 2018 from 192.168.2.1
WARNING: Your password has expired.
You must change your password now and login again!
Changing password for ubuntu.
(current) UNIX password: 
passwd: Authentication token manipulation error
passwd: password unchanged
Connection to 192.168.2.2 closed.
~ ❯❯❯ ssh ubuntu@192.168.2.2                                              ✘ 10 

ubuntu@192.168.2.2's password: 
You are required to change your password immediately (root enforced)
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1041-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 16:03:39 UTC 2018

  System load:  0.38              Processes:           110
  Usage of /:   4.6% of 28.81GB   Users logged in:     0
  Memory usage: 12%               IP address for eth0: 192.168.2.2
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jan 28 16:03:08 2018 from 192.168.2.1
WARNING: Your password has expired.
You must change your password now and login again!
Changing password for ubuntu.
(current) UNIX password: 
Enter new UNIX password: 
Retype new UNIX password: 
passwd: password updated successfully
Connection to 192.168.2.2 closed.
~ ❯❯❯ ssh ubuntu@192.168.2.2

ubuntu@192.168.2.2's password: 
Welcome to Ubuntu 18.04.3 LTS (GNU/Linux 4.15.0-1041-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 16:04:04 UTC 2018

  System load:  0.53              Processes:           113
  Usage of /:   4.6% of 28.81GB   Users logged in:     0
  Memory usage: 12%               IP address for eth0: 192.168.2.2
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jan 28 16:03:45 2018 from 192.168.2.1
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@ubuntu:~$ ls
ubuntu@ubuntu:~$ apt install ros-melodic-desktop-full
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
ubuntu@ubuntu:~$ sudo su ubuntu
ubuntu@ubuntu:~$ sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sh: 1: cannot create /etc/apt/sources.list.d/ros-latest.list: Permission denied
ubuntu@ubuntu:~$ apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key  421C365BD9FF1F717815A3895523BAEEB01FA116
Executing: /tmp/apt-key-gpghome.l4L0t8S36D/gpg.1.sh --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
gpg: key 5523BAEEB01FA116: public key "ROS Builder <rosbuild@ros.org>" imported
gpg: Total number processed: 1
gpg:               imported: 1
gpg: key 871920D1991BC93C was created 231 days in the future (time warp or clock problem)
gpg: key 871920D1991BC93C was created 231 days in the future (time warp or clock problem)
gpg: key 871920D1991BC93C was created 231 days in the future (time warp or clock problem)
/usr/bin/apt-key: 334: /usr/bin/apt-key: cannot create /etc/apt/trusted.gpg: Permission denied
cat: /tmp/apt-key-gpghome.l4L0t8S36D/gpgoutput.log: No such file or directory
ubuntu@ubuntu:~$ apt update
Reading package lists... Done
E: Could not open lock file /var/lib/apt/lists/lock - open (13: Permission denied)
E: Unable to lock directory /var/lib/apt/lists/
W: Problem unlinking the file /var/cache/apt/pkgcache.bin - RemoveCaches (13: Permission denied)
W: Problem unlinking the file /var/cache/apt/srcpkgcache.bin - RemoveCaches (13: Permission denied)
ubuntu@ubuntu:~$ apt upgrade
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
ubuntu@ubuntu:~$ apt install ros-melodic-desktop-full
E: Could not open lock file /var/lib/dpkg/lock-frontend - open (13: Permission denied)
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?
ubuntu@ubuntu:~$ sudo poweroff 
Connection to 192.168.2.2 closed by remote host.
Connection to 192.168.2.2 closed.
~ ❯❯❯ cd ~/.ssh                                                          ✘ 255 
~/.ssh ❯❯❯ sudo vim known_hosts
Password:
~/.ssh ❯❯❯ sudo vim known_hosts
~/.ssh ❯❯❯ cd
~ ❯❯❯ ssh ubuntu@192.168.2.2

^C
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 130 

ssh: connect to host 192.168.2.2 port 22: Host is down
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

ssh: connect to host 192.168.2.2 port 22: Host is down
~ ❯❯❯ cd ~/.ssh                                                          ✘ 255 
~/.ssh ❯❯❯ sudo vim known_hosts
Password:
~/.ssh ❯❯❯ cd
~ ❯❯❯ ssh ubuntu@192.168.2.2

^C
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 130 

ssh: connect to host 192.168.2.2 port 22: Host is down
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

The authenticity of host '192.168.2.2 (192.168.2.2)' can't be established.
ECDSA key fingerprint is SHA256:cCHLNrJJBvX0c/HU0nt4ZDc6H5G80W7sLFIF9KiDOBc.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.2.2' (ECDSA) to the list of known hosts.
ubuntu@192.168.2.2's password: 
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-1038-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Sun Jan 28 15:59:33 UTC 2018

  System load:  1.1                Processes:           117
  Usage of /:   10.0% of 28.80GB   Users logged in:     0
  Memory usage: 11%                IP address for eth0: 192.168.2.2
  Swap usage:   0%


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings


Last login: Sun Jan 28 16:00:05 2018
ubuntu@ubuntu:~$ ls
catkin_ws  ros_setup_scripts_Ubuntu18.04_server
ubuntu@ubuntu:~$ cd catkin_ws/
ubuntu@ubuntu:~/catkin_ws$ ls
build  devel  src
ubuntu@ubuntu:~/catkin_ws$ cd src/
ubuntu@ubuntu:~/catkin_ws/src$ ls
CMakeLists.txt
ubuntu@ubuntu:~/catkin_ws/src$ cd ..
ubuntu@ubuntu:~/catkin_ws$ catkin_make
Base path: /home/ubuntu/catkin_ws
Source space: /home/ubuntu/catkin_ws/src
Build space: /home/ubuntu/catkin_ws/build
Devel space: /home/ubuntu/catkin_ws/devel
Install space: /home/ubuntu/catkin_ws/install
####
#### Running command: "make cmake_check_build_system" in "/home/ubuntu/catkin_ws/build"
####
make: 警告: ファイル 'Makefile' の修正時刻 43725101 は未来の時刻です
make: 警告:  時刻のずれを検出. 不完全なビルド結果になるかもしれません.
####
#### Running command: "make -j4 -l4" in "/home/ubuntu/catkin_ws/build"
####
make: 警告: ファイル 'Makefile' の修正時刻 43725100 は未来の時刻です
make[1]: 警告: ファイル 'CMakeFiles/Makefile2' の修正時刻 43725100 は未来の時刻です
make[1]: 警告:  時刻のずれを検出. 不完全なビルド結果になるかもしれません.
make: 警告:  時刻のずれを検出. 不完全なビルド結果になるかもしれません.
ubuntu@ubuntu:~/catkin_ws$ cd
ubuntu@ubuntu:~$ timedatectl set-timezone Asia/Tokyo
==== AUTHENTICATING FOR org.freedesktop.timedate1.set-timezone ===
システムのタイムゾーンを設定するには認証が必要です。
Authenticating as: Ubuntu (ubuntu)
Password: 
==== AUTHENTICATION COMPLETE ===
ubuntu@ubuntu:~$ date
2018年  1月 29日 月曜日 01:03:33 JST
ubuntu@ubuntu:~$ vi /etc/systemd/timesyncd.conf
ubuntu@ubuntu:~$ vi /etc/systemd/timesyncd.conf
ubuntu@ubuntu:~$ sudo date 012122192020
2020年  1月 21日 火曜日 22:19:00 JST
ubuntu@ubuntu:~$ sudo date 012122202020
2020年  1月 21日 火曜日 22:20:00 JST
ubuntu@ubuntu:~$ cd catkin_ws/
ubuntu@ubuntu:~/catkin_ws$ catkin_make
Base path: /home/ubuntu/catkin_ws
Source space: /home/ubuntu/catkin_ws/src
Build space: /home/ubuntu/catkin_ws/build
Devel space: /home/ubuntu/catkin_ws/devel
Install space: /home/ubuntu/catkin_ws/install
####
#### Running command: "make cmake_check_build_system" in "/home/ubuntu/catkin_ws/build"
####
####
#### Running command: "make -j4 -l4" in "/home/ubuntu/catkin_ws/build"
####
ubuntu@ubuntu:~/catkin_ws$ ls
build  devel  src
ubuntu@ubuntu:~/catkin_ws$ source ~/.bashrc
ubuntu@ubuntu:~/catkin_ws$ sudo apt install ros-melodic-roslint 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  ros-melodic-roslint
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 0 個。
136 kB のアーカイブを取得する必要があります。
この操作後に追加で 622 kB のディスク容量が消費されます。
エラー:1 http://packages.ros.org/ros/ubuntu bionic/main armhf ros-melodic-roslint armhf 0.11.2-0bionic.20190602.081841
  404  Not Found [IP: 64.50.233.100 80]
E: http://packages.ros.org/ros/ubuntu/pool/main/r/ros-melodic-roslint/ros-melodic-roslint_0.11.2-0bionic.20190602.081841_armhf.deb の取得に失敗しました  404  Not Found [IP: 64.50.233.100 80]
E: いくつかのアーカイブを取得できません。apt-get update を実行するか --fix-missing オプションを付けて試してみてください。
ubuntu@ubuntu:~/catkin_ws$ apt-get update
パッケージリストを読み込んでいます... 完了
E: ロックファイル /var/lib/apt/lists/lock をオープンできません - open (13: 許可がありません)
E: ディレクトリ /var/lib/apt/lists/ をロックできません
W: ファイル /var/cache/apt/pkgcache.bin の削除中に問題が発生しました - RemoveCaches (13: 許可がありません)
W: ファイル /var/cache/apt/srcpkgcache.bin の削除中に問題が発生しました - RemoveCaches (13: 許可がありません)
ubuntu@ubuntu:~/catkin_ws$ sudo apt install ros-melodic-roslint 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  ros-melodic-roslint
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 0 個。
136 kB のアーカイブを取得する必要があります。
この操作後に追加で 622 kB のディスク容量が消費されます。
エラー:1 http://packages.ros.org/ros/ubuntu bionic/main armhf ros-melodic-roslint armhf 0.11.2-0bionic.20190602.081841
  404  Not Found [IP: 64.50.233.100 80]
E: http://packages.ros.org/ros/ubuntu/pool/main/r/ros-melodic-roslint/ros-melodic-roslint_0.11.2-0bionic.20190602.081841_armhf.deb の取得に失敗しました  404  Not Found [IP: 64.50.233.100 80]
E: いくつかのアーカイブを取得できません。apt-get update を実行するか --fix-missing オプションを付けて試してみてください。
ubuntu@ubuntu:~/catkin_ws$ sudo apt-get update
ヒット:1 http://ports.ubuntu.com/ubuntu-ports bionic InRelease                 
取得:2 http://packages.ros.org/ros/ubuntu bionic InRelease [4,669 B]           
取得:3 http://ports.ubuntu.com/ubuntu-ports bionic-updates InRelease [88.7 kB]
取得:4 http://ports.ubuntu.com/ubuntu-ports bionic-backports InRelease [74.6 kB]
取得:5 http://packages.ros.org/ros/ubuntu bionic/main armhf Packages [572 kB]
取得:6 http://ports.ubuntu.com/ubuntu-ports bionic-security InRelease [88.7 kB]
取得:7 http://ports.ubuntu.com/ubuntu-ports bionic/main Translation-ja [266 kB]
取得:8 http://ports.ubuntu.com/ubuntu-ports bionic/universe Translation-ja [1,140 kB]
取得:9 http://ports.ubuntu.com/ubuntu-ports bionic/multiverse Translation-ja [8,432 B]
取得:10 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe Sources [274 kB]
取得:11 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main Sources [303 kB]
取得:12 http://ports.ubuntu.com/ubuntu-ports bionic-updates/restricted Sources [6,536 B]
取得:13 http://ports.ubuntu.com/ubuntu-ports bionic-updates/multiverse Sources [5,844 B]
取得:14 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main armhf Packages [574 kB]
取得:15 http://ports.ubuntu.com/ubuntu-ports bionic-updates/main Translation-en [292 kB]
取得:16 http://ports.ubuntu.com/ubuntu-ports bionic-updates/restricted armhf Packages [6,820 B]
取得:17 http://ports.ubuntu.com/ubuntu-ports bionic-updates/restricted Translation-en [7,356 B]
取得:18 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe armhf Packages [876 kB]
取得:19 http://ports.ubuntu.com/ubuntu-ports bionic-updates/universe Translation-en [321 kB]
取得:20 http://ports.ubuntu.com/ubuntu-ports bionic-updates/multiverse armhf Packages [4,272 B]
取得:21 http://ports.ubuntu.com/ubuntu-ports bionic-updates/multiverse Translation-en [4,540 B]
取得:22 http://ports.ubuntu.com/ubuntu-ports bionic-backports/universe Sources [2,492 B]
取得:23 http://ports.ubuntu.com/ubuntu-ports bionic-backports/universe armhf Packages [4,040 B]
取得:24 http://ports.ubuntu.com/ubuntu-ports bionic-backports/universe Translation-en [1,900 B]
取得:25 http://ports.ubuntu.com/ubuntu-ports bionic-security/multiverse Sources [3,184 B]
取得:26 http://ports.ubuntu.com/ubuntu-ports bionic-security/main Sources [135 kB]
取得:27 http://ports.ubuntu.com/ubuntu-ports bionic-security/restricted Sources [4,544 B]
取得:28 http://ports.ubuntu.com/ubuntu-ports bionic-security/universe Sources [164 kB]
取得:29 http://ports.ubuntu.com/ubuntu-ports bionic-security/main armhf Packages [367 kB]
取得:30 http://ports.ubuntu.com/ubuntu-ports bionic-security/main Translation-en [198 kB]
取得:31 http://ports.ubuntu.com/ubuntu-ports bionic-security/restricted Translation-en [5,408 B]
取得:32 http://ports.ubuntu.com/ubuntu-ports bionic-security/universe armhf Packages [512 kB]
取得:33 http://ports.ubuntu.com/ubuntu-ports bionic-security/universe Translation-en [213 kB]
取得:34 http://ports.ubuntu.com/ubuntu-ports bionic-security/multiverse armhf Packages [2,076 B]
取得:35 http://ports.ubuntu.com/ubuntu-ports bionic-security/multiverse Translation-en [2,600 B]
6,536 kB を 21秒 で取得しました (305 kB/s)                                     
パッケージリストを読み込んでいます... 完了
ubuntu@ubuntu:~/catkin_ws$ sudo apt install ros-melodic-roslint 
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下のパッケージが新たにインストールされます:
  ros-melodic-roslint
アップグレード: 0 個、新規インストール: 1 個、削除: 0 個、保留: 256 個。
136 kB のアーカイブを取得する必要があります。
この操作後に追加で 623 kB のディスク容量が消費されます。
取得:1 http://packages.ros.org/ros/ubuntu bionic/main armhf ros-melodic-roslint armhf 0.11.2-0bionic.20191212.063407 [136 kB]
136 kB を 1秒 で取得しました (148 kB/s)       
以前に未選択のパッケージ ros-melodic-roslint を選択しています。
(データベースを読み込んでいます ... 現在 146025 個のファイルとディレクトリがインストールされています。)
.../ros-melodic-roslint_0.11.2-0bionic.20191212.063407_armhf.deb を展開する準備をしています ...
ros-melodic-roslint (0.11.2-0bionic.20191212.063407) を展開しています...
ros-melodic-roslint (0.11.2-0bionic.20191212.063407) を設定しています ...
ubuntu@ubuntu:~/catkin_ws$ cd ~/catkin_ws/src
ubuntu@ubuntu:~/catkin_ws/src$ git clone https://github.com/seiga-k/sysmon_ros.git
Cloning into 'sysmon_ros'...
remote: Enumerating objects: 78, done.
remote: Counting objects: 100% (78/78), done.
remote: Compressing objects: 100% (43/43), done.
remote: Total 268 (delta 38), reused 62 (delta 30), pack-reused 190
Receiving objects: 100% (268/268), 58.04 KiB | 373.00 KiB/s, done.
Resolving deltas: 100% (128/128), done.
ubuntu@ubuntu:~/catkin_ws/src$ cd ..
ubuntu@ubuntu:~/catkin_ws$ catkin_make -j 1
Base path: /home/ubuntu/catkin_ws
Source space: /home/ubuntu/catkin_ws/src
Build space: /home/ubuntu/catkin_ws/build
Devel space: /home/ubuntu/catkin_ws/devel
Install space: /home/ubuntu/catkin_ws/install
####
#### Running command: "cmake /home/ubuntu/catkin_ws/src -DCATKIN_DEVEL_PREFIX=/home/ubuntu/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/ubuntu/catkin_ws/install -G Unix Makefiles" in "/home/ubuntu/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/ubuntu/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/ubuntu/catkin_ws/devel;/opt/ros/melodic
-- This workspace overlays: /home/ubuntu/catkin_ws/devel;/opt/ros/melodic
-- Found PythonInterp: /usr/bin/python2 (found suitable version "2.7.15", minimum required is "2") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python2
-- Using Debian Python package layout
-- Using empy: /usr/bin/empy
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/ubuntu/catkin_ws/build/test_results
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python2 (found version "2.7.15") 
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Using Python nosetests: /usr/bin/nosetests-2.7
-- catkin 0.7.17
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - sysmon_ros
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'sysmon_ros'
-- ==> add_subdirectory(sysmon_ros)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- Boost version: 1.65.1
-- Found the following Boost libraries:
--   system
-- sysmon_ros: 2 messages, 0 services
-- Configuring done
-- Generating done
-- Build files have been written to: /home/ubuntu/catkin_ws/build
####
#### Running command: "make -j 1" in "/home/ubuntu/catkin_ws/build"
####
Scanning dependencies of target std_msgs_generate_messages_lisp
[  0%] Built target std_msgs_generate_messages_lisp
Scanning dependencies of target _sysmon_ros_generate_messages_check_deps_netif
[  0%] Built target _sysmon_ros_generate_messages_check_deps_netif
Scanning dependencies of target _sysmon_ros_generate_messages_check_deps_diskinfo
[  0%] Built target _sysmon_ros_generate_messages_check_deps_diskinfo
Scanning dependencies of target sysmon_ros_generate_messages_lisp
[  4%] Generating Lisp code from sysmon_ros/netif.msg
[  9%] Generating Lisp code from sysmon_ros/diskinfo.msg
[  9%] Built target sysmon_ros_generate_messages_lisp
Scanning dependencies of target std_msgs_generate_messages_cpp
[  9%] Built target std_msgs_generate_messages_cpp
Scanning dependencies of target sysmon_ros_generate_messages_cpp
[ 13%] Generating C++ code from sysmon_ros/netif.msg
[ 18%] Generating C++ code from sysmon_ros/diskinfo.msg
[ 18%] Built target sysmon_ros_generate_messages_cpp
Scanning dependencies of target std_msgs_generate_messages_eus
[ 18%] Built target std_msgs_generate_messages_eus
Scanning dependencies of target sysmon_ros_generate_messages_eus
[ 22%] Generating EusLisp code from sysmon_ros/netif.msg
[ 27%] Generating EusLisp code from sysmon_ros/diskinfo.msg
[ 31%] Generating EusLisp manifest code for sysmon_ros
[ 31%] Built target sysmon_ros_generate_messages_eus
Scanning dependencies of target std_msgs_generate_messages_nodejs
[ 31%] Built target std_msgs_generate_messages_nodejs
Scanning dependencies of target sysmon_ros_generate_messages_nodejs
[ 36%] Generating Javascript code from sysmon_ros/netif.msg
[ 40%] Generating Javascript code from sysmon_ros/diskinfo.msg
[ 40%] Built target sysmon_ros_generate_messages_nodejs
Scanning dependencies of target std_msgs_generate_messages_py
[ 40%] Built target std_msgs_generate_messages_py
Scanning dependencies of target sysmon_ros_generate_messages_py
[ 45%] Generating Python from MSG sysmon_ros/netif
[ 50%] Generating Python from MSG sysmon_ros/diskinfo
[ 54%] Generating Python msg __init__.py for sysmon_ros
[ 54%] Built target sysmon_ros_generate_messages_py
Scanning dependencies of target sysmon_ros_generate_messages
[ 54%] Built target sysmon_ros_generate_messages
Scanning dependencies of target roscpp_generate_messages_lisp
[ 54%] Built target roscpp_generate_messages_lisp
Scanning dependencies of target roscpp_generate_messages_py
[ 54%] Built target roscpp_generate_messages_py
Scanning dependencies of target rosgraph_msgs_generate_messages_cpp
[ 54%] Built target rosgraph_msgs_generate_messages_cpp
Scanning dependencies of target rosgraph_msgs_generate_messages_lisp
[ 54%] Built target rosgraph_msgs_generate_messages_lisp
Scanning dependencies of target rosgraph_msgs_generate_messages_nodejs
[ 54%] Built target rosgraph_msgs_generate_messages_nodejs
Scanning dependencies of target roscpp_generate_messages_nodejs
[ 54%] Built target roscpp_generate_messages_nodejs
Scanning dependencies of target rosgraph_msgs_generate_messages_eus
[ 54%] Built target rosgraph_msgs_generate_messages_eus
Scanning dependencies of target rosgraph_msgs_generate_messages_py
[ 54%] Built target rosgraph_msgs_generate_messages_py
Scanning dependencies of target roscpp_generate_messages_eus
[ 54%] Built target roscpp_generate_messages_eus
Scanning dependencies of target roscpp_generate_messages_cpp
[ 54%] Built target roscpp_generate_messages_cpp
Scanning dependencies of target tempmon
[ 59%] Building CXX object sysmon_ros/CMakeFiles/tempmon.dir/src/tempmon.cpp.o
[ 63%] Linking CXX executable /home/ubuntu/catkin_ws/devel/lib/sysmon_ros/tempmon
[ 63%] Built target tempmon
Scanning dependencies of target netmon
[ 68%] Building CXX object sysmon_ros/CMakeFiles/netmon.dir/src/netmon.cpp.o
[ 72%] Linking CXX executable /home/ubuntu/catkin_ws/devel/lib/sysmon_ros/netmon
[ 72%] Built target netmon
Scanning dependencies of target cpumon
[ 77%] Building CXX object sysmon_ros/CMakeFiles/cpumon.dir/src/cpumon.cpp.o
[ 81%] Linking CXX executable /home/ubuntu/catkin_ws/devel/lib/sysmon_ros/cpumon
[ 81%] Built target cpumon
Scanning dependencies of target memmon
[ 86%] Building CXX object sysmon_ros/CMakeFiles/memmon.dir/src/memmon.cpp.o
[ 90%] Linking CXX executable /home/ubuntu/catkin_ws/devel/lib/sysmon_ros/memmon
[ 90%] Built target memmon
Scanning dependencies of target diskmon
[ 95%] Building CXX object sysmon_ros/CMakeFiles/diskmon.dir/src/diskmon.cpp.o
In file included from /usr/include/boost/bind.hpp:22:0,
                 from /opt/ros/melodic/include/ros/publisher.h:35,
                 from /opt/ros/melodic/include/ros/node_handle.h:32,
                 from /opt/ros/melodic/include/ros/ros.h:45,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/boost/bind/bind_cc.hpp: In function ‘boost::_bi::bind_t<R, R (*)(B1), typename boost::_bi::list_av_1<A1>::type> boost::bind(R (*)(B1), A1) [with R = ros::SerializedMessage; B1 = const sysmon_ros::diskinfo_<std::allocator<void> >&; A1 = boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >]’:
/usr/include/boost/bind/bind_cc.hpp:26:5: note: parameter passing for argument of type ‘boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >’ changed in GCC 7.1
     BOOST_BIND(BOOST_BIND_ST R (BOOST_BIND_CC *f) (B1), A1 a1)
     ^
In file included from /usr/include/boost/bind/bind.hpp:2126:0,
                 from /usr/include/boost/bind.hpp:22,
                 from /opt/ros/melodic/include/ros/publisher.h:35,
                 from /opt/ros/melodic/include/ros/node_handle.h:32,
                 from /opt/ros/melodic/include/ros/ros.h:45,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/boost/bind/bind_cc.hpp:30:58: note: parameter passing for argument of type ‘boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >’ changed in GCC 7.1
     return _bi::bind_t<R, F, list_type> (f, list_type(a1));
                                                          ^
In file included from /usr/include/boost/bind.hpp:22:0,
                 from /opt/ros/melodic/include/ros/publisher.h:35,
                 from /opt/ros/melodic/include/ros/node_handle.h:32,
                 from /opt/ros/melodic/include/ros/ros.h:45,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/boost/bind/bind.hpp: In constructor ‘boost::_bi::list1<A1>::list1(A1) [with A1 = boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >]’:
/usr/include/boost/bind/bind.hpp:231:14: note: parameter passing for argument of type ‘boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >’ changed in GCC 7.1
     explicit list1( A1 a1 ): base_type( a1 ) {}
              ^~~~~
/usr/include/boost/bind/bind.hpp:231:44: note: parameter passing for argument of type ‘boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >’ changed in GCC 7.1
     explicit list1( A1 a1 ): base_type( a1 ) {}
                                            ^
In file included from /usr/include/boost/bind/bind.hpp:47:0,
                 from /usr/include/boost/bind.hpp:22,
                 from /opt/ros/melodic/include/ros/publisher.h:35,
                 from /opt/ros/melodic/include/ros/node_handle.h:32,
                 from /opt/ros/melodic/include/ros/ros.h:45,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/boost/bind/storage.hpp: In constructor ‘boost::_bi::storage1<A1>::storage1(A1) [with A1 = boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >]’:
/usr/include/boost/bind/storage.hpp:42:14: note: parameter passing for argument of type ‘boost::reference_wrapper<const sysmon_ros::diskinfo_<std::allocator<void> > >’ changed in GCC 7.1
     explicit storage1( A1 a1 ): a1_( a1 ) {}
              ^~~~~~~~
In file included from /usr/include/c++/7/vector:69:0,
                 from /usr/include/boost/math/special_functions/math_fwd.hpp:26,
                 from /usr/include/boost/math/special_functions/round.hpp:15,
                 from /opt/ros/melodic/include/ros/time.h:58,
                 from /opt/ros/melodic/include/ros/ros.h:38,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/c++/7/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::emplace_back(_Args&& ...) [with _Args = {long long int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’:
/usr/include/c++/7/bits/vector.tcc:105:21: note: parameter passing for argument of type ‘__gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >’ changed in GCC 7.1
    _M_realloc_insert(end(), std::forward<_Args>(__args)...);
    ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/usr/include/c++/7/bits/vector.tcc: In member function ‘void std::vector<_Tp, _Alloc>::_M_realloc_insert(std::vector<_Tp, _Alloc>::iterator, _Args&& ...) [with _Args = {long long int}; _Tp = long long int; _Alloc = std::allocator<long long int>]’:
/usr/include/c++/7/bits/vector.tcc:394:7: note: parameter passing for argument of type ‘std::vector<long long int>::iterator {aka __gnu_cxx::__normal_iterator<long long int*, std::vector<long long int> >}’ changed in GCC 7.1
       vector<_Tp, _Alloc>::
       ^~~~~~~~~~~~~~~~~~~
In file included from /usr/include/c++/7/vector:63:0,
                 from /usr/include/boost/math/special_functions/math_fwd.hpp:26,
                 from /usr/include/boost/math/special_functions/round.hpp:15,
                 from /opt/ros/melodic/include/ros/time.h:58,
                 from /opt/ros/melodic/include/ros/ros.h:38,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/c++/7/bits/stl_uninitialized.h: In function ‘_ForwardIterator std::__uninitialized_move_if_noexcept_a(_InputIterator, _InputIterator, _ForwardIterator, _Allocator&) [with _InputIterator = long long int*; _ForwardIterator = long long int*; _Allocator = std::allocator<long long int>]’:
/usr/include/c++/7/bits/stl_uninitialized.h:312:69: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
   _GLIBCXX_MAKE_MOVE_IF_NOEXCEPT_ITERATOR(__last), __result, __alloc);
                                                                     ^
/usr/include/c++/7/bits/stl_uninitialized.h: In function ‘_ForwardIterator std::__uninitialized_copy_a(_InputIterator, _InputIterator, _ForwardIterator, std::allocator<_Tp>&) [with _InputIterator = std::move_iterator<long long int*>; _ForwardIterator = long long int*; _Tp = long long int]’:
/usr/include/c++/7/bits/stl_uninitialized.h:287:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
     __uninitialized_copy_a(_InputIterator __first, _InputIterator __last,
     ^~~~~~~~~~~~~~~~~~~~~~
/usr/include/c++/7/bits/stl_uninitialized.h:287:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
/usr/include/c++/7/bits/stl_uninitialized.h:289:63: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
     { return std::uninitialized_copy(__first, __last, __result); }
                                                               ^
/usr/include/c++/7/bits/stl_uninitialized.h: In function ‘_ForwardIterator std::uninitialized_copy(_InputIterator, _InputIterator, _ForwardIterator) [with _InputIterator = std::move_iterator<long long int*>; _ForwardIterator = long long int*]’:
/usr/include/c++/7/bits/stl_uninitialized.h:115:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
     uninitialized_copy(_InputIterator __first, _InputIterator __last,
     ^~~~~~~~~~~~~~~~~~
/usr/include/c++/7/bits/stl_uninitialized.h:115:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
/usr/include/c++/7/bits/stl_uninitialized.h:134:41: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
  __uninit_copy(__first, __last, __result);
                                         ^
/usr/include/c++/7/bits/stl_uninitialized.h: In static member function ‘static _ForwardIterator std::__uninitialized_copy<true>::__uninit_copy(_InputIterator, _InputIterator, _ForwardIterator) [with _InputIterator = std::move_iterator<long long int*>; _ForwardIterator = long long int*]’:
/usr/include/c++/7/bits/stl_uninitialized.h:99:9: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
         __uninit_copy(_InputIterator __first, _InputIterator __last,
         ^~~~~~~~~~~~~
/usr/include/c++/7/bits/stl_uninitialized.h:99:9: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
/usr/include/c++/7/bits/stl_uninitialized.h:101:53: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
         { return std::copy(__first, __last, __result); }
                                                     ^
In file included from /usr/include/c++/7/bits/char_traits.h:39:0,
                 from /usr/include/c++/7/string:40,
                 from /opt/ros/melodic/include/ros/platform.h:38,
                 from /opt/ros/melodic/include/ros/time.h:53,
                 from /opt/ros/melodic/include/ros/ros.h:38,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/c++/7/bits/stl_algobase.h: In function ‘_OI std::copy(_II, _II, _OI) [with _II = std::move_iterator<long long int*>; _OI = long long int*]’:
/usr/include/c++/7/bits/stl_algobase.h:446:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
     copy(_II __first, _II __last, _OI __result)
     ^~~~
/usr/include/c++/7/bits/stl_algobase.h:446:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
In file included from /usr/include/c++/7/bits/stl_algobase.h:67:0,
                 from /usr/include/c++/7/bits/char_traits.h:39,
                 from /usr/include/c++/7/string:40,
                 from /opt/ros/melodic/include/ros/platform.h:38,
                 from /opt/ros/melodic/include/ros/time.h:53,
                 from /opt/ros/melodic/include/ros/ros.h:38,
                 from /home/ubuntu/catkin_ws/src/sysmon_ros/src/diskmon.cpp:6:
/usr/include/c++/7/bits/stl_iterator.h: In function ‘decltype (std::__miter_base(__it.base())) std::__miter_base(std::move_iterator<_IteratorL>) [with _Iterator = long long int*]’:
/usr/include/c++/7/bits/stl_iterator.h:1244:5: note: parameter passing for argument of type ‘std::move_iterator<long long int*>’ changed in GCC 7.1
     __miter_base(move_iterator<_Iterator> __it)
     ^~~~~~~~~~~~
[100%] Linking CXX executable /home/ubuntu/catkin_ws/devel/lib/sysmon_ros/diskmon
[100%] Built target diskmon
ubuntu@ubuntu:~/catkin_ws$ roscore
... logging to /home/ubuntu/.ros/log/93f574f0-3c52-11ea-a3d5-b827eb1fb365/roslaunch-ubuntu-2643.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://localhost:36807/
ros_comm version 1.14.3


SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.3

NODES

auto-starting new master
process[master]: started with pid [2655]
ROS_MASTER_URI=http://localhost:11311/

setting /run_id to 93f574f0-3c52-11ea-a3d5-b827eb1fb365
process[rosout-1]: started with pid [2667]
started core service [/rosout]
packet_write_poll: Connection to 192.168.2.2 port 22: Host is down
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

ssh: connect to host 192.168.2.2 port 22: Operation timed out
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 255 

^C
~ ❯❯❯ ssh ubuntu@192.168.2.2                                             ✘ 130 

ubuntu@192.168.2.2's password: 
Welcome to Ubuntu 18.04.2 LTS (GNU/Linux 4.15.0-1038-raspi2 armv7l)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Mon Jan 29 00:58:53 JST 2018

  System load:  2.63               Processes:           119
  Usage of /:   10.3% of 28.80GB   Users logged in:     0
  Memory usage: 11%                IP address for eth0: 192.168.2.2
  Swap usage:   0%


  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

262 個のパッケージがアップデート可能です。
95 個のアップデートはセキュリティアップデートです。


Last login: Mon Jan 29 01:00:24 2018
ubuntu@ubuntu:~$ ls
catkin_ws  ros_setup_scripts_Ubuntu18.04_server
ubuntu@ubuntu:~$ cd catkin_ws/
ubuntu@ubuntu:~/catkin_ws$ ls
build  devel  src
ubuntu@ubuntu:~/catkin_ws$ cd src/
ubuntu@ubuntu:~/catkin_ws/src$ ls
CMakeLists.txt  LED_ultrasonic  mypkg  sysmon_ros
ubuntu@ubuntu:~/catkin_ws/src$ cd LED_ultrasonic/
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ ls
CMakeLists.txt  package.xml  scripts  src
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ rm -r src
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ ls
CMakeLists.txt  package.xml  scripts
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ vim package.xml 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ vim package.xml 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ cd scripts/
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim led.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ sudo py
py3clean             pybuild              pydoc2.7             pygettext3           pyshell              python2.7            python3-jsonpatch    python3.6m           pywrap
py3compile           pyclean              pydoc3               pygettext3.6         python               python2.7-config     python3-jsonpointer  python3.6m-config    pywxrc
py3versions          pycompile            pydoc3.6             pygmentize           python-config        python3              python3-jsonschema   python3m             
pyalacarte           pycrust              pygettext            pyhtmlizer3          python2              python3-config       python3.6            python3m-config      
pyalamode            pydoc                pygettext2.7         pyjwt3               python2-config       python3-jsondiff     python3.6-config     pyversions           
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ sudo py
py3clean             pybuild              pydoc2.7             pygettext3           pyshell              python2.7            python3-jsonpatch    python3.6m           pywrap
py3compile           pyclean              pydoc3               pygettext3.6         python               python2.7-config     python3-jsonpointer  python3.6m-config    pywxrc
py3versions          pycompile            pydoc3.6             pygmentize           python-config        python3              python3-jsonschema   python3m             
pyalacarte           pycrust              pygettext            pyhtmlizer3          python2              python3-config       python3.6            python3m-config      
pyalamode            pydoc                pygettext2.7         pyjwt3               python2-config       python3-jsondiff     python3.6-config     pyversions           
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ sudo python3 led.py 
^Cubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim led.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
led.py  ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ cd ..
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ cd scripts/
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
led.py  ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ chmod +x ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
led.py  ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ cd ..
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ ls
CMakeLists.txt  package.xml  scripts
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ rosrun LED_ultrasonic ultrasonic.py 
Unable to register with master node [http://localhost:11311]: master may not be running yet. Will keep trying.
^CTraceback (most recent call last):
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 5, in <module>
    rospy.init_node('ultrasonic')
  File "/opt/ros/melodic/lib/python2.7/dist-packages/rospy/client.py", line 336, in init_node
    raise rospy.exceptions.ROSInitException("Failed to initialize time. Please check logs for additional details")
rospy.exceptions.ROSInitException: Failed to initialize time. Please check logs for additional details
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ rosrun LED_ultrasonic ultrasonic.py 
Traceback (most recent call last):
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 6, in <module>
    pub = rospy.Publisher('distance', Int32, queue_size=1)
NameError: name 'Int32' is not defined
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ cd scripts/
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls]

Command 'ls]' not found, did you mean:

  command 'lsh' from deb lsh-client
  command 'lsm' from deb lsm
  command 'ls' from deb coreutils
  command 'lsw' from deb suckless-tools
  command 'lsc' from deb livescript

Try: sudo apt install <deb name>

ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
led.py  ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ ls
led.py  ultrasonic.py
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ chmod +x ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    except KeyboardInterrupt:
         ^
SyntaxError: invalid syntax
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ vim ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ chmod +x ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    
                     ^
SyntaxError: invalid syntax
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic/scripts$ cd ..
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    
                     ^
SyntaxError: invalid syntax
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ cd ..
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    
                     ^
SyntaxError: invalid syntax
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/
led.py         ultrasonic.py  
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    
                                ^
IndentationError: unexpected unindent
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 48
    
                                ^
IndentationError: unexpected unindent
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
Traceback (most recent call last):
  File "/home/ubuntu/catkin_ws/src/LED_ultrasonic/scripts/ultrasonic.py", line 6, in <module>
    pub = rospy.Publisher('distance', float32, queue_size=1)
NameError: name 'float32' is not defined
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/led.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
^C


ubuntu@ubuntu:~/catkin_ws/src$ 
ubuntu@ubuntu:~/catkin_ws/src$ 
ubuntu@ubuntu:~/catkin_ws/src$ 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/led.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
^Cubuntu@ubuntu:~/catkin_ws/srcvim LED_ultrasonic/scripts/ultrasonicic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ vim LED_ultrasonic/scripts/ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ rosrun LED_ultrasonic ultrasonic.py 
ubuntu@ubuntu:~/catkin_ws/src$ ls
CMakeLists.txt  LED_ultrasonic  mypkg  sysmon_ros
ubuntu@ubuntu:~/catkin_ws/src$ cd LED_ultrasonic/
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ ls
CMakeLists.txt  package.xml  scripts
ubuntu@ubuntu:~/catkin_ws/src/LED_ultrasonic$ vim CMakeLists.txt 

## Mark executables and/or libraries for installation
# install(TARGETS ${PROJECT_NAME} ${PROJECT_NAME}_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_LED_ultrasonic.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
                                                              197,1        末尾
