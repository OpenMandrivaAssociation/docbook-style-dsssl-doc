%define name docbook-style-dsssl-doc
%define version 1.79
%define release %mkrel 11

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.79-10mdv2011.0
+ Revision: 663841
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.79-9mdv2011.0
+ Revision: 604808
- rebuild

* Sun Jan 17 2010 Funda Wang <fwang@mandriva.org> 1.79-8mdv2010.1
+ Revision: 492815
- fix spec file

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.79-7mdv2010.0
+ Revision: 413371
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.79-6mdv2009.1
+ Revision: 350832
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.79-5mdv2009.0
+ Revision: 220676
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.79-4mdv2008.1
+ Revision: 149205
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Apr 28 2007 Adam Williamson <awilliamson@mandriva.org> 1.79-3mdv2008.0
+ Revision: 18856
- clean spec; rebuild for new era


* Mon Apr 03 2006 Camille Begnis <camille@mandriva.com> 1.79-2mdk
- Fix license to please rpmlint
- rebuild

* Fri Nov 05 2004 Camille Begnis <camille@mandrakesoft.com> 1.79-1mdk
- 1.79

* Mon Apr 05 2004 Camille Begnis <camille@mandrakesoft.com> 1.78-2mdk
- Rebuild

