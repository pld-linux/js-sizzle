%define		rev	4251a83f9cdc9edc4e5814691f0071b51b766e4d
Summary:	A pure-JavaScript CSS selector engine
Name:		sizzle
Version:	1.0
Release:	0.1
License:	MIT, BSD, and GPL
Group:		Applications/WWW
Source0:	http://download.github.com/jeresig-%{name}-%{rev}.zip
# Source0-md5:	73b356e1769768e854d8202d4410959d
URL:		http://www.sizzlejs.com/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
A pure-JavaScript CSS selector engine designed to be easily dropped in
to a host library.

%prep
%setup -q -n jeresig-%{name}-%{rev}

%build
%{__make} jquery

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a sizzle.js jquery-sizzle.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE test/index.html
%{_appdir}
