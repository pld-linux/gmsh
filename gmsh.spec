Summary:	A 3D mesh generator with pre- and post-processing facilities
Summary(pl):	Generator siatki 3D zawieraj±cy pre/post procesor
Name:		gmsh
Version:	1.50.0
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	http://www.geuz.org/gmsh/src/%{name}-%{version}-source.tgz
# Source0-md5:	91547444733a7a043b5de994d3330218
URL:		http://www.geuz.org/gmsh/
BuildRequires:	OpenGL-devel
BuildRequires:	fltk-gl-devel
BuildRequires:	gsl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmsh is an automatic three-dimensional finite element mesh generator,
primarily Delaunay, with built-in pre- and post-processing facilities.
Its primal design goal is to provide a simple meshing tool for
academic test cases with parametric input and up to date visualization
capabilities. One of the strengths of Gmsh is its ability to respect a
characteristic length field for the generation of adapted meshes on
lines, surfaces and volumes. Gmsh requires OpenGL (or Mesa) to be
installed on your system.

%description -l pl
Gmsh jest automatycznym generatorem trójwymiarowej siatki elementów
skoñczonych (g³ównie Delaunay), z wbudowanym pre/post procesorem.
G³ównym zadaniem przy projektowaniu Gmsh by³o stworzenie prostego
narzêdzia wykorzystywanego w testach akademickich, do generownia
siatki, z parametrycznym wej¶ciem i mo¿liwo¶ci± wizualizacji wyników
na bie¿±co. Jedn± z mocnych stron Gmesh jest mo¿liwo¶æ okre¶lenia
d³ugo¶ci generowanego elementu, która zostanie zastosowana do
dyskretyzacji lini, powierzchni i objêto¶ci. Gmesh wymaga OpenGL (lub
Mesy) zainstalowanej w twoim systemie.

%prep
%setup -q

%build
%configure
%{__make}
%{__make} converters
%{__make} doc-info

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_infodir},%{_mandir}/man1}

install bin/{gmsh,dxf2geo} $RPM_BUILD_ROOT%{_bindir}
install doc/gmsh.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/texinfo/gmsh.info* $RPM_BUILD_ROOT%{_infodir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO doc/CREDITS doc/FAQ doc/VERSIONS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/gmsh.1*
%{_infodir}/*.info*
