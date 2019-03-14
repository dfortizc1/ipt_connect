# -*- coding: utf-8 -*-

# Views parameters
app_version = "IPTdev"[3:]     # keyword for url parsing
# TODO:
# The construction `"IPTdev"[3:]` above is a dirty hack.
# We need to mention `IPTdev` to enable automated cloning,
# but we have to set version to `dev` to satisfy some pieces of code.
# No idea how is it handled for FPT.
# To be refactored:
# grep "app_version"


NAME = {
    'short': 'IPT dev',
    'full': 'International Physicists\' Tournament - Development Instance'
}

# Models parameters
npf = 4                 # Number of Physics fights
with_final_pf = True    # Is there a Final Fight ?
reject_malus = 0.2      # Malus for too many rejections
npfreject_max = 3       # Maximum number of tactical rejection (per fight)
netreject_max = 1       # Maximum number of eternal rejection

# Personal ranking
personal_ranking = {
    'active': False,
    'rep_threshold': 5,
    'opp_threshold': 5,
    'rev_threshold': 5,
    'rep_coeff': 3,
    'opp_coeff': 2,
    'rev_coeff': 1
}

# Calculating the mean
mean = 'ipt_mean'  # String with name of function for calculating mean (ipt_mean or iypt_mean)

# Is the fight status displayed?
# Looks like there are some problems with it, so making it switchable
display_pf_status = True

# Do we respect pools?
# If true, then the pool is displayed in ranking table
# and the 'Ranking' menu item leads to poolranking
enable_pools = True
