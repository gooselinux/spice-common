
%define tarname spice-common
%define tarversion 0.4.2

%define patchid 7
Name:           spice-common
Version:        0.4.2
Release:        %{patchid}%{?dist}
Summary:        Spice common sources used to build spice-server and spice-client
Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://www.spice-space.org/
Source0:        %{tarname}-%{tarversion}.tar.bz2

BuildRoot:      %{_tmppath}/%{tarname}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  i686 x86_64

BuildRequires:  autoconf automake

Patch1: spice-common-01-new-migration-process.patch
Patch2: spice-common-02-make-opengl-optional-disabled-by-default.patch
Patch3: spice-common-03-fix-unsafe-guest-host-data-handling.patch



%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package should only be used for building other spice packages.
Not intended to be installed on user machines.

%package devel
Summary:  Spice common sources used to build spice-server and spice-client
Requires:  pkgconfig

%description devel
This package should only be used for building other spice packages.
Not intended to be installed on user machines.
Contains common source code files.

%prep
%setup -q -n %{tarname}-%{tarversion}
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
CFLAGS="%{optflags}"; CFLAGS="${CFLAGS/-Wall/}"; export CFLAGS;
CXXFLAGS="%{optflags}"; CXXFLAGS="${CXXFLAGS/-Wall/}"; export CXXFLAGS;
FFLAGS="%{optflags}"; FFLAGS="${FFLAGS/-Wall/}"; export FFLAGS;
autoreconf -i -f
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
#mkdir -p $RPM_BUILD_ROOT/usr/lib64/pkgconfig/
#cp spice-common.pc $RPM_BUILD_ROOT/usr/lib64/pkgconfig/


%clean
rm -rf $RPM_BUILD_ROOT


%files devel
%defattr(-, root, root, 0755)
%doc COPYING INSTALL README
%{_prefix}/src/spice-common/
%{_libdir}/pkgconfig/spice-common.pc

%changelog
* Fri Jul 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-7
 - fix unsafe guest/host data handling
 Resolves: #568811

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-6
 - make opengl optional, disabled by default
 Resolves: #482556

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-5
 - Generate auto* generated files (e.g. Makefile.in)
Resolves: #579330

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-4
 - new migration process
Resolves: #576033

* Mon Mar  1 2010 Uri Lublin <uril@redhat.com> - 0.4.2-3
 - Remove BuildRequires: pkgconfig
 - Move Requires: pkgconfig to -devel subpackage.
Related: #543948

* Wed Jan 13 2009 Uri Lublin <uril@redhat.com> - 0.4.2-2
 - ExclusiveArch:  i686 x86_64
Related: #549806
* Wed Jan 13 2009 Uri Lublin <uril@redhat.com> - 0.4.2-1
 - Build -devel package.
Related: #549806
* Mon Jan 11 2009 Uri Lublin <uril@redhat.com> - 0.4.2-0
 - First spec for 0.4.2
Related: #549806

