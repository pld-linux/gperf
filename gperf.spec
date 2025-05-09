Summary:	A perfect hash function generator
Summary(pl.UTF-8):	Generator funkcji haszujących
Name:		gperf
Version:	3.3
Release:	1
License:	GPL v3+
Group:		Development/Tools
Source0:	https://ftp.gnu.org/gnu/gperf/%{name}-%{version}.tar.gz
# Source0-md5:	31753b021ea78a21f154bf9eecb8b079
Patch0:		%{name}-info.patch
Patch1:		%{name}-no_dvi_html.patch
URL:		http://www.gnu.org/software/gperf/
BuildRequires:	libstdc++-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gperf is a perfect hash function generator written in C++. Simply
stated, a perfect hash function is a hash function and a data
structure that allows recognition of a key word in a set of words
using exactly one probe into the data structure.

%description -l pl.UTF-8
Gperf jest napisanym w C++ generatorem doskonałych funkcji
haszujących. Doskonała funkcja haszująca to funkcja haszująca oraz
struktura danych, pozwalająca rozpoznać słowo kluczowe w zbiorze słów
wykorzystując dokładnie jedną próbę.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/gperf
%{_mandir}/man1/gperf.1*
%{_infodir}/gperf.info*
