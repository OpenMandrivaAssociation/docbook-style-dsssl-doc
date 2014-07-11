Summary:	Documentation for DocBook dssl stylesheets
Name:		docbook-style-dsssl-doc
Version:	1.79
Release:	17
Group:		Books/Computer books
License:	Artistic like
Url:		http://sourceforge.net/projects/docbook/
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-dsssl-doc-%{version}.tar.bz2
BuildArch:	noarch

%description
This package contains the documentation for these stylesheets:
structure, customization, etc.

%prep
%setup -n docbook-dsssl-%{version} -q

%files
%doc doc docsrc

