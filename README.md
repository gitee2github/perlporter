# perlporter

#### Description
perl pacaking automation tool

perlporter is derived from cpanspec tool, It helps to build perl modules to be rpm package automatically, It can be used to resolve the build dependencies of perl modules

#### Installation
Install below software before using this tool

1.  yum install cpan
2.  yum install perl
3.  yum install perl-YAML
4.  python3 setup.py install

#### Preparation
Execute the following command to complete the system configuration

1.  sudo cpan
2.  install Archive::Tar
3.  install Archive::Zip
4.  install Text::Autoformat
5.  install Parse::CPAN::Packages

#### Instructions

perlporter is a tool to create spec file and create rpm for perl modules
For more details, please use perlporter -h

Example: to generate spec file for perl-Clone:

```
perlporter -s Clone
```

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request

#### How to create a rpm file,Take perl-XXX as an example

1.  Create spec file:              perlporter --spec XXX
2.  The root path for rpm build:   perlporter --root XXX
3.  Build and Install rpm package: perlporter -B XXX
4.  For more detail:               perlporter -h


