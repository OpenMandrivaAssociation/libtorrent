%define major 21
%define libname %mklibname torrent %major
%define libnamedev %mklibname -d torrent

Name:		libtorrent
Version:	0.13.8
Release:	2
Summary:	BitTorrent library written in C++ for *nix
License:	GPLv2+
Group:		Networking/File transfer
URL:		https://github.com/rakshasa/libtorrent
Source0:	http://rtorrent.net/downloads/%{name}-%{version}.tar.gz
#Source0:   https://github.com/rakshasa/rtorrent/releases/download/v0.9.7/libtorrent-0.13.7.tar.gz
Patch0:		libtorrent-0.13.1-fix-linking.patch
Patch1:		libtorrent-0.13.7-no-bogus--Lusrlib.patch
BuildRequires:	sigc++2.0-devel
BuildRequires: 	pkgconfig(openssl)
#gw only if autoconf/automake is called:
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	cppunit-devel
BuildRequires:  pkgconfig(zlib)

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
%autosetup -p1
autoreconf -fi

%build
#gw work around compiler bug according to the home page:
export CFLAGS=$(echo %optflags|sed s/O2/O3/)
export CXXFLAGS=$(echo %optflags|sed s/O2/O3/)
%configure --with-posix-fallocate
%make_build

%install 
%make_install
  
%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{libnamedev}
%{_libdir}/lib*.so
%if %mdvver <= 201100
%{_libdir}/lib*.la
%endif
%{_includedir}/torrent/
%{_libdir}/pkgconfig/%{name}.pc
