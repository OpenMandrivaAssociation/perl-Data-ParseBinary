%define upstream_name    Data-ParseBinary
%define upstream_version 0.31

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Data::ParseBinary::(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Parsing UNIX's SO files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
# perl virtual package is not versioned
BuildRequires:	perl-Math-BigInt >= 1.993.0
BuildArch:	noarch

%description
This module is a Perl Port for PyConstructs
http://construct.wikispaces.com/

This module enables writing declarations for simple and complex binary
structures, parsing binary to hash/array data structure, and building
binary data from hash/array data structure.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.310.0-2mdv2011.0
+ Revision: 657405
- rebuild for updated spec-helper

* Sat Mar 19 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.310.0-1
+ Revision: 647030
- update to new version 0.31

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.300.0-1
+ Revision: 638475
- update to new version 0.3

* Fri Dec 24 2010 Shlomi Fish <shlomif@mandriva.org> 0.290.0-1mdv2011.0
+ Revision: 624669
- import perl-Data-ParseBinary

