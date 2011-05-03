%define name docbook-style-dsssl-doc
%define version 1.79
%define release %mkrel 10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Books/Computer books
Summary:	Documentation for DocBook dssl stylesheets
License:	Artistic like
URL:		http://sourceforge.net/projects/docbook/
BuildRoot:	%{_tmppath}/%{name}-buildroot 
BuildArch:	noarch
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%{version}.tar.bz2

%description
This package contains the documentation for these stylesheets:
structure, customization, etc.

%prep
%setup -n docbook-dsssl-%{version} -q

%files
%defattr (-,root,root)
%doc doc docsrc
