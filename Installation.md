# Server Installation #

  * Extract the archive into `/home/dbackup`
  * Add the following line to `/etc/services`:
```
dbackup     38771/tcp
```

  * Add the following line to `/etc/inetd.conf` (or create a config file if you use xinetd):
```
38771           stream  tcp     nowait  root    /home/dbackup/dbackup_server
```
  * Copy the default configuration file `dbackup_config` to `/etc/dbackup/config` and edit it. Specifically, make sure the `backup_root` directive is correct, and add regexes to match all the backup client IP addresses to `ip_allow`.
  * Restart inetd or xinetd (`killall -HUP inetd`).
  * Add the following lines to `/etc/crontab` to verify and report on the backups.
```
0 00 * * 0 root /home/dbackup/dbackup_verify
0 09 * * * root /home/dbackup/dbackup_report
```

# Client Installation #

  * Extract the archive into `/home/dbackup`
  * Add the following line to `/etc/services`:
```
dbackup     38771/tcp
```

  * Copy the default configuration file `dbackup-client.conf` to `/etc/dbackup-client/config`, and edit it. At the very least you need to change the backup servers to your own.
  * Create an entry in `/etc/crontab`. It's worthwhile staggering the start times of multiple clients.
```
0 2 * * * root /home/dbackup/dbackup backup /path/to/filesystem /another/filesystem
```
  * Wait for the backup to happen. The server will only produce output if there is an error, which cron will mail to root. If you want to force a report to be generated every run, add the "`-r`" flag to the command line.