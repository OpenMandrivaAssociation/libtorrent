%define major 10
%define libname %mklibname torrent %major
%define libnamedev %mklibname -d torrent
%define release %mkrel 1

Name: libtorrent
Version: 0.12.1
Release: %release
Summary: BitTorrent library written in C++ for *nix
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL
Group: Networking/File transfer
URL: http://libtorrent.rakshasa.no/
Source0: http://libtorrent.rakshasa.no/downloads/libtorrent-%{version}.tar.gz
BuildRequires: sigc++2.0-devel
BuildRequires: openssl-devel
BuildRequires: automake libtool

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

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)
%configure2_5x
%make

%install 
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
%makeinstall
  
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*a
%{_includedir}/torrent/
%{_libdir}/pkgconfig/%{name}.pc
