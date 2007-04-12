%define Name docbook-style-dsssl-doc
%define Version 1.79

Name:		%{Name}
Version:	%{Version}
Release:	2mdk
Group       	: Books/Computer books

Summary         : Documentation for DocBook dssl stylesheets

License   	: Artistic like
URL         	: http://sourceforge.net/projects/docbook/

BuildRoot   	: %{_tmppath}/%{name}-buildroot 

BuildArch	: noarch
Source0		: http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%{Version}.tar.bz2

%define sgmlbase %{_prefix}/share/sgml/ 

%description
This package contains the documentation for these stylesheets:
structure, customization, etc.

%prep
%setup -n docbook-dsssl-%{Version} -q
%setup -T -D -n docbook-dsssl-%{Version}

%build

%install

%clean
DESTDIR=$RPM_BUILD_ROOT
rm -rf $DESTDIR


%files
%defattr (-,root,root)
%doc doc docsrc


