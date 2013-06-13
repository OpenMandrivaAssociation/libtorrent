%define major 17
%define libname %mklibname torrent %major
%define libnamedev %mklibname -d torrent

Name:		libtorrent
Version:	0.13.3
Release:	1
Summary:	BitTorrent library written in C++ for *nix
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://libtorrent.rakshasa.no/
Source0:	http://libtorrent.rakshasa.no/downloads/libtorrent-%{version}.tar.gz
Patch0:		libtorrent-0.13.1-fix-linking.patch
BuildRequires:	sigc++2.0-devel
BuildRequires: 	openssl-devel
#gw only if autoconf/automake is called:
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	cppunit-devel

%description
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

Authors:
--------
    Jari Sundell <jaris@ifi.uio.no>

%package -n %{libname}
Summary:	BitTorrent library written in C++ for *nix
Group:		System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %libname
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

Authors:
--------
    Jari Sundell <jaris@ifi.uio.no>

%package -n %{libnamedev}
Summary:	BitTorrent library written in C++ for *nix
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %name 10

%description -n %libnamedev
LibTorrent is a BitTorrent library written in C++ for *nix. It is designed to
avoid redundant copying and storing of data that other clients and libraries
suffer from. Licensed under the GPL.

Basic features have been implemented and a ncurses client is included. Sloppy
and biased test runs have shown that transferring a 200 MB file with libTorrent
uses 1/4 of the CPU time that the official BitTorrent client requires.

The library and client are under heavy development. They are stable enough to
handle any torrents I throw at them these days. 

Authors:
--------
    Jari Sundell <jaris@ifi.uio.no>

%prep
%setup -q
%apply_patches

autoreconf -fi

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)
%configure2_5x --with-posix-fallocate
%make

%install 
%makeinstall_std
  
%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/lib*.so
%if %mdvver <= 201100
%{_libdir}/lib*.la
%endif
%{_includedir}/torrent/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Jun 01 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.2-1
+ Revision: 801718
- update to new version 0.13.2

* Thu Apr 05 2012 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.1-1
+ Revision: 789337
- update build deps
- fix linking
- update to new version 0.13.1
- prepare for backports

* Fri Dec 30 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.13.0-1
+ Revision: 748245
- remove libtool archive
- new version

* Fri Jun 24 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.9-1
+ Revision: 686871
- update to new version 0.12.9

* Mon May 09 2011 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.8-1
+ Revision: 672984
- new version
- new major

* Mon Nov 01 2010 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.7-1mdv2011.0
+ Revision: 591449
- new version
- new major

* Mon Apr 19 2010 Funda Wang <fwang@mandriva.org> 0.12.6-2mdv2010.1
+ Revision: 536660
- rebuild

* Mon Dec 07 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.6-1mdv2010.1
+ Revision: 474371
- update to new version 0.12.6

* Fri Nov 20 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.12.5-2mdv2010.1
+ Revision: 467683
- Enable use of posix_fallocate.

* Tue Jun 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.5-1mdv2010.0
+ Revision: 388749
- update to new version 0.12.5

* Thu Nov 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.4-1mdv2009.1
+ Revision: 305256
- update to new version 0.12.4

* Thu Sep 18 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.3-1mdv2009.0
+ Revision: 285599
- new version
- drop all patches
- new major

* Fri Aug 08 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.2-2mdv2009.0
+ Revision: 268130
- update license
- sync patches with Gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri May 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.2-1mdv2009.0
+ Revision: 204939
- new version
- new major

* Wed Apr 23 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.1-1mdv2009.0
+ Revision: 196741
- new version
- new major

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.12.0-2mdv2008.1
+ Revision: 170960
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Jan 29 2008 GÃ¶tz Waschk <waschk@mandriva.org> 0.12.0-1mdv2008.1
+ Revision: 159932
- new version
- new major

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 26 2007 Funda Wang <fwang@mandriva.org> 0.11.9-1mdv2008.1
+ Revision: 102270
- New version 0.11.9

* Tue Oct 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.8-1mdv2008.1
+ Revision: 96135
- new version

* Mon Aug 20 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.7-1mdv2008.0
+ Revision: 67210
- new version

* Thu Aug 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.6-1mdv2008.0
+ Revision: 58071
- new version
- new devel name

* Tue Jul 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.5-1mdv2008.0
+ Revision: 47379
- new version


* Thu Mar 29 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.4-1mdv2007.1
+ Revision: 149305
- new version
- remove build fix
- don't own the pkgconfig dir (AdamW)

* Sun Jan 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.2-1mdv2007.1
+ Revision: 114534
- new version

* Sun Dec 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.1-1mdv2007.1
+ Revision: 102954
- new version

* Wed Dec 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.11.0-1mdv2007.1
+ Revision: 96388
- new version
- new major
- update file list

* Wed Nov 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10.4-2mdv2007.1
+ Revision: 78121
- fix optimization flags

* Sun Oct 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10.4-1mdv2007.1
+ Revision: 73634
- new version
- Import libtorrent

* Thu Oct 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10.3-1mdv2007.1
- New version 0.10.3

* Fri Sep 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.10.2-1mdv2007.0
- New version 0.10.2

* Sat Aug 19 2006 Götz Waschk <waschk@mandriva.org> 0.10.1-1mdv2007.0
- new major
- New release 0.10.1

* Tue Jul 18 2006 Götz Waschk <waschk@mandriva.org> 0.10.0-1mdv2007.0
- new major
- fix build
- New release 0.10.0

* Thu May 25 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.3-1mdk
- New release 0.9.3

* Mon May 22 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.2-1mdk
- New release 0.9.2

* Mon May 08 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.9.1-1mdk
- New release 0.9.1

* Mon Apr 10 2006 Götz Waschk <waschk@mandriva.org> 0.9.0-1mdk
- new major
- New release 0.9.0

* Mon Feb 20 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.5-1mdk
- New release 0.8.5

* Mon Jan 23 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.3-1mdk
- New release 0.8.3

* Thu Jan 12 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.2-1mdk
- New release 0.8.2

* Wed Dec 21 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.8.1-1mdk
- New release 0.8.1

* Mon Nov 28 2005 Götz Waschk <waschk@mandriva.org> 0.8.0-1mdk
- major 6
- New release 0.8.0

* Thu Oct 20 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.6-1mdk
- New release 0.7.6

* Sat Oct 01 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.5-1mdk
- New release 0.7.5

* Mon Sep 19 2005 GÃ¶tz Waschk <waschk@mandriva.org> 0.7.4-1mdk
- New release 0.7.4

* Tue Sep 06 2005 Götz Waschk <waschk@mandriva.org> 0.7.3-1mdk
- major 5
- New release 0.7.3

* Thu Aug 25 2005 Götz Waschk <waschk@mandriva.org> 0.7.2-1mdk
- drop patch
- New release 0.7.2

* Fri Jul 29 2005 Götz Waschk <waschk@mandriva.org> 0.7.0-2mdk
- bugfix from 0.7.0-1

* Thu Jul 21 2005 Götz Waschk <waschk@mandriva.org> 0.7.0-1mdk
- mkrel
- major 4
- New release 0.7.0

* Thu Jul 14 2005 Götz Waschk <waschk@mandriva.org> 0.6.7-1mdk
- New release 0.6.7

* Tue Jun 28 2005 Götz Waschk <waschk@mandriva.org> 0.6.6-1mdk
- New release 0.6.6

* Tue Jun 21 2005 Götz Waschk <waschk@mandriva.org> 0.6.5-1mdk
- New release 0.6.5

* Thu Jun 09 2005 Götz Waschk <waschk@mandriva.org> 0.6.4-1mdk
- New release 0.6.4

* Thu Jun 02 2005 Götz Waschk <waschk@mandriva.org> 0.6.3-1mdk
- new major
- New release 0.6.3

* Sat May 07 2005 Götz Waschk <waschk@mandriva.org> 0.6.2-1mdk
- New release 0.6.2

* Fri Apr 29 2005 Götz Waschk <waschk@mandriva.org> 0.6.1-1mdk
- New release 0.6.1

* Sun Apr 24 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-2mdk
- add provides on libtorrent to the library package

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 0.6.0-1mdk
- New release 0.6.0

* Sat Apr 16 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.5.5-1mdk
- New release 0.5.5

* Wed Mar 30 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 0.5.4-1mdk
- New release 0.5.4

* Sun Mar 13 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-2mdk
- fix buildrequires

* Wed Mar 09 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.1-1mdk
- remove rtorrent
- New release 0.5.1

* Sun Feb 27 2005 Götz Waschk <waschk@linux-mandrake.com> 0.5.0-1mdk
- New release 0.5.0

* Sun Feb 20 2005 Götz Waschk <waschk@linux-mandrake.com> 0.4.11-1mdk
- initial mdk package

* Sat Dec 18 2004 - darix@irssi.org
- initial package

