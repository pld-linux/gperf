Summary: A perfect hash function generator.
Name: gperf
Version: 2.7
Release: 5
Copyright: GPL
Source: ftp://prep.ai.mit.edu/pub/gnu/gperf-2.7.tar.gz
Patch0: gperf-2.7-egcs.patch
Group: Development/Tools
Prereq:		/usr/sbin/fix-info-dir	
BuildRoot: /var/tmp/gperf-root

%description
Gperf is a perfect hash function generator written in C++.  Simply
stated, a perfect hash function is a hash function and a data structure
that allows recognition of a key word in a set of words using exactly
one probe into the data structure.

Install gperf if you need a program that generates perfect hash functions.

%prep
%setup -q
%patch0 -p1 -b .egcs

%build
CC=egcs CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr

make prefix=$RPM_BUILD_ROOT/usr install

gzip -9nf $RPM_BUILD_ROOT/usr/info/gperf.info*
rm -rf $RPM_BUILD_ROOT/usr/man/{dvi,html}
strip $RPM_BUILD_ROOT/usr/bin/gperf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%preun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(-,root,root)
%doc README NEWS doc/gperf.html
/usr/bin/gperf
/usr/man/man1/gperf.1
/usr/info/gperf.info*
