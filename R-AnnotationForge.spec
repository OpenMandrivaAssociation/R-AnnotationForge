%global packname  AnnotationForge
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.4.0
Release:          1
Summary:          Code for Building Annotation Database Packages
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz

Requires:         R-methods R-utils R-BiocGenerics R-Biobase R-AnnotationDbi R-org.Hs.eg.db 
Requires:         R-methods R-utils R-DBI R-RSQLite R-BiocGenerics R-Biobase 
Requires:         R-DBI R-RSQLite R-XML R-RCurl R-hgu95av2.db R-human.db0 R-affy R-Homo.sapiens R-hom.Hs.inp.db R-GO.db R-BiocStyle R-knitr 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-utils R-BiocGenerics R-Biobase R-AnnotationDbi R-org.Hs.eg.db
BuildRequires:    R-methods R-utils R-DBI R-RSQLite R-BiocGenerics R-Biobase 
BuildRequires:   R-DBI R-RSQLite R-XML R-RCurl R-hgu95av2.db R-human.db0 R-affy R-Homo.sapiens R-hom.Hs.inp.db R-GO.db R-BiocStyle R-knitr 
%description
Provides code for generating Annotation packages and their databases. 
Packages produced are intended to be used with AnnotationDbi.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
