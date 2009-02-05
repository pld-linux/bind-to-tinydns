Summary:	Convert DNS zone files in BIND format to tinydns format
Name:		bind-to-tinydns
Version:	0.4.3
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://www.erat.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	92657532ac03c439c85156554351b154
URL:		http://www.erat.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a program that parses zone files used by the BIND DNS server
and converts them to the native format of the tinydns component of Dan
Bernstein's djbdns DNS server.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D bind-to-tinydns $RPM_BUILD_ROOT%{_bindir}/bind-to-tinydns

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc example-bind-zone.db README
%attr(755,root,root) %{_bindir}/bind-to-tinydns
