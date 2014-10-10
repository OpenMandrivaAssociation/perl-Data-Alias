%define	module	Data-Alias
%define upstream_version 1.18

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Comprehensive set of aliasing operations
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Alias-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

%description
Aliasing is the phenomenon where two different expressions actually refer
to the same thing. Modifying one will modify the other, and if you take a
reference to both, the two values are the same.

%prep
%setup -q -n %{module}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data
