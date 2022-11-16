%define upstream_name    Data-ParseBinary

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Data::ParseBinary::(.*)\\)'
%endif

Name:		perl-%{upstream_name}
Version:	0.31
Release:	6

Summary:	Parsing UNIX's SO files
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{version}.tar.gz
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
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
