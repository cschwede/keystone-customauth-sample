Openstack Keystone custom password check example
================================================


[![Build Status](https://travis-ci.org/cschwede/keystone-customauth-sample.svg)](https://travis-ci.org/cschwede/keystone-customauth-sample)

Example Keystone middleware to use external password authentication in Keystone.
This example actually doesn't check the password, but grants access to everyone
during Happy Hour.

Quick Install
-------------

1) Install the example:

    git clone git://github.com/cschwede/keystone-customauth-sample.git
    cd keystone-customauth-sample
    sudo python setup.py install

2) Set the customauth middleware as identity provider in
/etc/keystone/keystone.conf:

    [identity]
    driver=customauth.middleware.HappyHourIdentity

3) Restart Keystone server: 

    service openstack-keystone restart

Done!
