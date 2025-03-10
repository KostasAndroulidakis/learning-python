"""Calculates the likely spread of a virus in a population."""

import random

# Likelihood someone infects a susceptible member they come in contact with.
transmission_rate = 1 / 20

# Average number of days before someone is no longer contagious.
days_to_recover = 5

def spread(num_infected, num_can_catch_virus, population_size, daily_contacts):
    """Returns the number of new infections over one day. May be zero."""
    percent_can_catch_virus = num_can_catch_virus / population_size

    total_newly_infected = 0
    for member in range(num_infected):
        # Each member's contact rate varies, averaging out to daily_contacts.
        num_contacts = random.randint(0, daily_contacts * 2)
        contacts_can_catch_virus = num_contacts * percent_can_catch_virus
        newly_infected = contacts_can_catch_virus * transmission_rate

        total_newly_infected = total_newly_infected + newly_infected

    return min(round(total_newly_infected), num_can_catch_virus)

def recover(num_infected):
    """Returns the number of recovered infections over one day. May be zero."""
    newly_recovered = 0
    for member in range(num_infected):
        # There's a 1 / days_to_recover chance of recovering on any given day.
        recovery_state = random.randint(1, days_to_recover)
        if recovery_state == 1:
            newly_recovered = newly_recovered + 1
    return newly_recovered
