Summary:	A perfect hash function generator
Summary(pl):	Generator funkcji haszuj±cych
Name:		gperf
Version:	2.7.2
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	ftp://ftp.gnu.org/pub/gnu/gperf/%{name}-%{version}.tar.gz
# Source0-md5:	e501acc2e18eed2c8f25ca0ac2330d68
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_dvi_html.patch
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%description -l pl
Gperf jest napisanym w C++ generatorem doskona³ych funkcji
haszuj±cych. Doskona³a funkcja haszuj±ca to funkcja haszuj±ca oraz
struktura danych, pozwalaj±ca rozpoznaæ s³owo kluczowe w zbiorze s³ów
wykorzystuj±c dok³adnie jedn± próbê.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} %{!?debug:-fno-rtti -fno-exceptions -fno-implicit-templates}"
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS
%attr(755,root,root) %{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
