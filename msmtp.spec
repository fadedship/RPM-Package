Name:           msmtp
Version:        1.8.22
Release:        1%{?dist}
Summary:        msmtp 

License:	GPLv3+
URL:            https://marlam.de/%{name}/
Source0:        https://marlam.de/%{name}/releases/%{name}-%{version}.tar.xz

BuildRequires:  make
BuildRequires:	gcc
BuildRequires:	cpp

%description
msmtp install tool


%prep
%autosetup


%build
gettextize -f
autoreconf -fi
./configure
make

%install
%make_install


%files
/usr/local/bin/%{name}
   /usr/lib/debug/usr/local/bin/msmtpd-1.8.22-1.el8.x86_64.debug
   /usr/local/bin/msmtpd
   /usr/local/share/info/dir
   /usr/local/share/info/msmtp.info
   /usr/local/share/locale/de/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/eo/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/fr/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/pt_BR/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/sr/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/ta/LC_MESSAGES/msmtp.mo
   /usr/local/share/locale/uk/LC_MESSAGES/msmtp.mo
   /usr/local/share/man/man1/msmtp.1
   /usr/local/share/man/man1/msmtpd.1

%changelog
* Wed Aug 31 2022 root
- 
