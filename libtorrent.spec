%define major 14
%define libname %mklibname torrent %major
%define libnamedev %mklibname -d torrent
%define release %mkrel 1

Name: libtorrent
Version: 0.13.2
Release: %release
Summary: BitTorrent library written in C++ for *nix
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPLv2+
Group: Networking/File transfer
URL: http://libtorrent.rakshasa.no/
Source0: http://libtorrent.rakshasa.no/downloads/libtorrent-%{version}.tar.gz
Patch0: libtorrent-0.13.1-fix-linking.patch
BuildRequires: sigc++2.0-devel
BuildRequires: openssl-devel
#gw only if autoconf/automake is called:
BuildRequires: automake libtool cppunit-devel


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

%package -n %libname
Summary: BitTorrent library written in C++ for *nix
Group: System/Libraries
Provides: %name = %version-%release

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

%package -n %libnamedev
Summary: BitTorrent library written in C++ for *nix
Group: Development/C++
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d %name 10

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
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
%makeinstall
  
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/lib*.so
%if %mdvver <= 201100
%{_libdir}/lib*.la
%endif
%{_includedir}/torrent/
%{_libdir}/pkgconfig/%{name}.pc
