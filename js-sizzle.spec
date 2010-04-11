Summary:	A pure-JavaScript CSS selector engine
Name:		js-sizzle
Version:	1.0
Release:	0.2
License:	MIT, BSD, and GPL v2
Group:		Applications/WWW
Source0:	http://download.github.com/jeresig-sizzle-852d3d0.zip
# Source0-md5:	8524ff0dcd1aefdbd653b16e3636dc5c
URL:		http://www.sizzlejs.com/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
A pure-JavaScript CSS selector engine designed to be easily dropped in
to a host library.

%prep
%setup -qc
mv jeresig-sizzle-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a sizzle.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{_appdir}
