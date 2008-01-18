#------------------------------------------------------------------------------
# Copyright (c) 2008, Riverbank Computing Limited
# All rights reserved.
#
# This software is provided without warranty under the terms of the BSD
# license included in enthought/LICENSE.txt and may be redistributed only
# under the conditions described in the aforementioned license.  The license
# is also available online at http://www.enthought.com/licenses/BSD.txt
# Thanks for using Enthought open source!
#
# Author: Riverbank Computing Limited
# Description: <Enthought permissions package component>
#------------------------------------------------------------------------------


# Enthought library imports.
from enthought.pyface.action.api import Action
from enthought.traits.api import Bool, Instance, Interface, List

# Local imports.
from i_permission import IPermission
from i_user_manager import IUserManager


class IPermissionsPolicy(Interface):
    """The interface implemented by a permissions policy.  A permissions policy
    completely defines how permissions and authorisation is handled.  A default
    permissions policy is provided, but it may be replaced using the
    permissions manager.
    """

    # Set if bootstrap permissions should be automatically enabled if the
    # policy is bootstrapping (ie. when no policy or user data has been
    # defined).  Bootstrap permissions are normally attached to actions used to
    # define policy and user data.  Normally this is True, unless policy and
    # user data is to be managed by an external application.
    allow_bootstrap_perms = Bool(True)

    # The list of PyFace policy management actions implemented by this policy.
    management_actions = List(Instance(Action))

    # The list of all permissions that the policy enforces.
    perms = List(Instance(IPermission))

    # The user manager.  The policy uses this to add, modify and delete users.
    user_manager = Instance(IUserManager)

    def bootstrapping(self):
        """Return True if the permissions policy is bootstrapping.  Typically
        this is when no policy or user data has been defined."""

    def check_perms(self, *perms):
        """Check that the current user has one or more of the given
        permissions and return True if they have.  perms is a list of objects
        that implement the IPermission interface.
        """