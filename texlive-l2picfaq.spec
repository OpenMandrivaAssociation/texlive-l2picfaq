# revision 19601
# category Package
# catalog-ctan /info/l2picfaq/german
# catalog-date 2010-08-29 15:51:21 +0200
# catalog-license fdl
# catalog-version 1.50
Name:		texlive-l2picfaq
Version:	1.50
Release:	9
Summary:	LaTeX pictures "how-to" (German)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/l2picfaq/german
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2picfaq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/l2picfaq.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.50-2
+ Revision: 753060
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.50-1
+ Revision: 718789
- texlive-l2picfaq
- texlive-l2picfaq
- texlive-l2picfaq
- texlive-l2picfaq

