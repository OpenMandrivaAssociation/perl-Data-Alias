%define	module	Data-Alias
%define upstream_version 1.18

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Comprehensive set of aliasing operations
License:	GPLv1+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Alias-%{upstream_version}.tar.gz
Patch0:		Data-Alias-1.16-string-format-fix.patch

BuildRequires:	perl-devel

%description
Aliasing is the phenomenon where two different expressions actually refer
to the same thing. Modifying one will modify the other, and if you take a
reference to both, the two values are the same.

%prep
%setup -q -n %{module}-%{upstream_version}
%patch0 -p1 -b .str_fmt~

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


%changelog
* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.160.0-1
+ Revision: 770573
- apply string format fix
- update url
- new version
- cleanup spec
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.150.0-1
+ Revision: 686625
- update to new version 1.15

* Mon May 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.140.0-1
+ Revision: 662053
- update to new version 1.14

* Thu Feb 24 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.120.0-1
+ Revision: 639633
- update to new version 1.12

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.110.0-1
+ Revision: 634221
- update to new version 1.11

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 601864
- update to new version 1.10

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 598083
- update to new version 1.09

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 595093
- update to new version 1.08

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12
    - rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 401671
- rebuild using %%perl_convert_version
- fixed license field

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 1.07-2mdv2010.0
+ Revision: 375956
- rebuild

* Sun May 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2010.0
+ Revision: 371457
- import perl-Data-Alias


* Sun May 03 2009 cpan2dist 1.07-1mdv
- initial mdv release, generated with cpan2dist


