Summary:	A perfect hash function generator
Name:		gperf
Version:	2.7
Release:	6
Copyright:	GPL
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://prep.ai.mit.edu/pub/gnu/gperf/%{name}-%{version}.tar.gz
Patch0:		gperf-egcs.patch
Patch1:		gperf-DESTDIR.patch
Patch2:		gperf-info.patch
Patch3:		gperf-no_dvi_html.patch
BuildRequires:	libstdc++-devel
Prereq:		/usr/sbin/fix-info-dir	
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Gperf is a perfect hash function generator written in C++. Simply stated, a
perfect hash function is a hash function and a data structure that allows
recognition of a key word in a set of words using exactly one probe into the
data structure.

Install gperf if you need a program that generates perfect hash functions.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates"
LDFLAGS="-s"
export CXXFLAGS LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT{%{_infodir}/*,%{_mandir}/man1/*} \
	README NEWS

#strip $RPM_BUILD_ROOT/usr/bin/gperf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
