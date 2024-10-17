Name:		texlive-l2picfaq
Version:	19601
Release:	2
Summary:	LaTeX pictures "how-to" (German)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/l2picfaq/german
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2picfaq.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2picfaq.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The document (in German) is a collection of "how-to" notes
about LaTeX and pictures. The aim of the document is to provide
a solution, in the form of some sample code, for every problem.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/l2picfaq/README
%doc %{_texmfdistdir}/doc/latex/l2picfaq/ctanlion.pdf
%doc %{_texmfdistdir}/doc/latex/l2picfaq/gfdl.tex
%doc %{_texmfdistdir}/doc/latex/l2picfaq/l2picfaq.pdf
%doc %{_texmfdistdir}/doc/latex/l2picfaq/l2picfaq.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
