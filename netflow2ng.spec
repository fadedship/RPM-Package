Name:           netflow2ng
Version:        0.0.3
Release:        1%{?dist}
Summary:        netflow

License:        GPLv3+
URL:            https://github.com/synfinatic/netflow2ng/
Source0:        https://github.com/synfinatic/netflow2ng/archive/refs/tags/v0.0.3.tar.gz

BuildRequires:  go
BuildRequires:	make

%description
%global debug_package %{nil}

%prep
%autosetup


%build
make

%install
mkdir -p %{buildroot}/%{_bindir}

install -m 0755 dist/netflow2ng-0.0.3 %{buildroot}/%{_bindir}/%{name}


%files
%{_bindir}/%{name}
%license LICENSE


%changelog
* Wed Aug 31 2022 root
- 
