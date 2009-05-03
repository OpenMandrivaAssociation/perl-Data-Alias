%define module   Data-Alias
%define version    1.07
%define release    %mkrel 1

%define Werror_cflags %nil

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Comprehensive set of aliasing operations
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Data/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Aliasing is the phenomenon where two different expressions actually refer
to the same thing. Modifying one will modify the other, and if you take a
reference to both, the two values are the same.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%optflags"

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Data
%{perl_vendorarch}/auto/Data

