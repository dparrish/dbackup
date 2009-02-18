Version:	1.1.0
Summary:	Disk-based backup Server
Name:		dbackup
Release:	1
License:	GPL
Group:		Applications/Backup
Source:		%{name}-%{version}.tar.gz
URL:		http://www.dparrish.com/dbackup.html
Packager:	David Parrish <david-dbackup@dparrish.com>
Vendor:		David Parrish <david-dbackup@dparrish.com>
BuildRoot:	/var/tmp/%{name}-buildroot/
Prefix:		/usr
Requires:	perl

%description
dbackup is a disk-based client-server backup system for Linux or other
UNIX systems.

It works on the principal that disks are cheaper and more reliable
than tapes.

Backups are started by cron probably on a daily basis by the client. The
client backs up individual filesystems / directories with tar and sends
the result to the server, which stores them in a simple tree-based
directory structure.

Restores are trivial, either by using the supplied restore client,
or by simply copying the appropriate tar files off the server and
uncompressing them.

%package server
Summary:	Disk-based backup server
Group:		Applications/Backup
Requires:	xinetd

%package client
Summary:	Disk-based backup client
Group:		Applications/Backup

%changelog
* Thu Oct 26 2006 David Parrish <david-dbackup@dparrish.com>
- Release 1.1.0
- Major rewrite which breaks backward compatibility
- Script locations have changed, and client scripts merged into a single file

* Tue Jun 13 2006 David Parrish <david-dbackup@dparrish.com>
- Release 1.0.4
- Put configuration in /etc/dbackup/config
- Add POD documentation for all tools - Jari Aalto

* Fri May 9 2003 David Parrish <david-dbackup@dparrish.com>
- Release 1.0.3
- Specify binmode :raw for all filehandles. Perl 5.8.0 on RH 8/9 uses utf8 by default.
- Fix localisation problem with df output
- Include installation note for dbackup_config

* Thu May 8 2003 David Parrish <david-dbackup@dparrish.com>
- Release 1.0.2
- First RPM release
- Add entry to /etc/services
- Requires xinetd
- Changed default paths for binaries and config files
- Made safe_mode not the default in dbackup_archive. Use -s to enable it
- More stats in dbackup_report
- dbackup_server copes better with out-of-space errors
- dbackup_verify is now a 2 stage check. testing, verbose and skip md5 are now options
- Fix bug with filesystem handling in dbackup_client


%prep

%setup

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/state/dbackup
install -D -o root -g root -m 0755 dbackup_server $RPM_BUILD_ROOT/%{prefix}/sbin/dbackup_server
install -D -o root -g root -m 0755 dbackup_report $RPM_BUILD_ROOT/%{prefix}/sbin/dbackup_report
install -D -o root -g root -m 0755 dbackup_verify $RPM_BUILD_ROOT/%{prefix}/sbin/dbackup_verify
install -D -o root -g root -m 0600 dbackup_config $RPM_BUILD_ROOT/etc/dbackup/config
install -D -o root -g root -m 0600 dbackup-client.conf $RPM_BUILD_ROOT/etc/dbackup-client/config
install -D -o root -g root -m 0600 rpm/dbackup.xinetd $RPM_BUILD_ROOT/etc/xinetd.d/dbackup
install -D -o root -g root -m 0600 rpm/dbackup-server.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/dbackup_server
install -D -o root -g root -m 0755 dbackup $RPM_BUILD_ROOT/%{prefix}/bin/dbackup
install -D -o root -g root -m 0600 rpm/dbackup-client.logrotate $RPM_BUILD_ROOT/etc/logrotate.d/dbackup_client

%clean
rm -rf $RPM_BUILD_ROOT

%description server
dbackup is a disk-based client-server backup system for Linux or other
UNIX systems.

It works on the principal that disks are cheaper and more reliable
than tapes.

Backups are started by cron probably on a daily basis by the client. The
client backs up individual filesystems / directories with tar and sends
the result to the server, which stores them in a simple tree-based
directory structure.

Restores are trivial, either by using the supplied restore client,
or by simply copying the appropriate tar files off the server and
uncompressing them.

This package provides the server portion of dbackup. It includes archiving,
reporting and verification.

%description client
dbackup is a disk-based client-server backup system for Linux or other
UNIX systems.

It works on the principal that disks are cheaper and more reliable
than tapes.

Backups are started by cron probably on a daily basis by the client. The
client backs up individual filesystems / directories with tar and sends
the result to the server, which stores them in a simple tree-based
directory structure.

Restores are trivial, either by using the supplied restore client,
or by simply copying the appropriate tar files off the server and
uncompressing them.

This package provides the client portion of dbackup, including backup
and restore.

%post client
	grep -q '^dbackup' /etc/services
	if [ $? -ne 0 ]; then
		echo "dbackup		38771/tcp			# dbackup" >> /etc/services
	fi

%files client
%defattr(-, root, root)
%{prefix}/bin/dbackup
%dir /var/state/dbackup
%config(noreplace) /etc/dbackup-client/config
%config(noreplace) /etc/logrotate.d/dbackup_client

%files server
%defattr(-, root, root)
%{prefix}/sbin/dbackup_server
%{prefix}/sbin/dbackup_verify
%{prefix}/sbin/dbackup_report
%dir /var/state/dbackup
%doc INSTALL Changes LICENSE
%config(noreplace) /etc/dbackup/config
%config(noreplace) /etc/xinetd.d/dbackup
%config(noreplace) /etc/logrotate.d/dbackup_server

