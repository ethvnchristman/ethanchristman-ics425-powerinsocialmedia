# TikTok Stakeholder Power Model
# ICS 425 - Power in Social Media Assignment
# Ethan C. — Student ID: 28538244

# =============================================================================
# PART 1: EXISTING STAKEHOLDER STRUCTURE
# =============================================================================

class Stakeholder:
    """Base class for all TikTok stakeholders."""
    def __init__(self, name, data_access, revenue_share, decision_power):
        self.name = name
        self.data_access = data_access        # 0-10: visibility into platform data
        self.revenue_share = revenue_share    # 0-10: share of platform-generated revenue
        self.decision_power = decision_power  # 0-10: influence over platform rules/algorithm
        self.autonomy = self._calc()

    def _calc(self):
        return round((self.data_access + self.revenue_share + self.decision_power) / 3, 2)

    def describe(self):
        print(f"\n--- {self.name} ---")
        print(f"  Data Access:    {self.data_access}/10")
        print(f"  Revenue Share:  {self.revenue_share}/10")
        print(f"  Decision Power: {self.decision_power}/10")
        print(f"  Autonomy Score: {self.autonomy}/10")


class User(Stakeholder):
    """Everyday TikTok users who consume content."""
    def __init__(self, name="General User"):
        super().__init__(name, data_access=1, revenue_share=1, decision_power=1)
        self.can_export_data = False
        self.content_ownership = "None (consumer only)"

    def describe(self):
        super().describe()
        print(f"  Can Export Data:   {self.can_export_data}")


class Creator(User):
    """Users who produce content. Subclass of User."""
    def __init__(self, name="Creator"):
        super().__init__(name)
        self.data_access = 3      # Some analytics via Creator Tools
        self.revenue_share = 2    # Creator Rewards Program, but discretionary
        self.decision_power = 2   # No formal governance role
        self.autonomy = self._calc()
        self.content_ownership = "Retained, but platform holds broad license"
        self.monetization_control = "Algorithm-dependent, platform can change at any time"

    def describe(self):
        super().describe()
        print(f"  Content Ownership:      {self.content_ownership}")
        print(f"  Monetization Control:   {self.monetization_control}")


class Influencer(Creator):
    """Creators with large followings who earn primarily via brand deals.
    Subclass of Creator — same platform constraints, more economic independence."""
    def __init__(self, name="Influencer"):
        super().__init__(name)
        self.data_access = 3      # Same platform analytics access
        self.revenue_share = 4    # Higher due to brand deal income (external)
        self.decision_power = 3   # Slightly more informal leverage via public backlash
        self.autonomy = self._calc()
        self.primary_income = "Brand partnerships (external to platform)"

    def describe(self):
        super().describe()
        print(f"  Primary Income:   {self.primary_income}")


class Advertiser(Stakeholder):
    """Brands that purchase ad placements on TikTok."""
    def __init__(self, name="Advertiser"):
        super().__init__(name, data_access=6, revenue_share=0, decision_power=6)
        self.targeting = "Behavioral + demographic"

    def describe(self):
        super().describe()
        print(f"  Targeting:   {self.targeting}")


class PlatformOwner(Stakeholder):
    """ByteDance / TikTok USDS — owns and controls the platform."""
    def __init__(self, name="TikTok Platform Owner"):
        super().__init__(name, data_access=10, revenue_share=10, decision_power=10)
        self.algorithm_transparency = "Opaque — no external audit"
        self.content_license = "Worldwide, royalty-free license to all user content"
        self.monetization_terms = "Set unilaterally, can be changed or ended at any time"

    def describe(self):
        super().describe()
        print(f"  Algorithm Transparency:  {self.algorithm_transparency}")
        print(f"  Content License:         {self.content_license}")
        print(f"  Monetization Terms:      {self.monetization_terms}")


class Regulator(Stakeholder):
    """Government bodies attempting to oversee TikTok."""
    def __init__(self, name="Government Regulator"):
        super().__init__(name, data_access=2, revenue_share=0, decision_power=4)
        self.enforcement = "Fragmented across jurisdictions, slow relative to platform"

    def describe(self):
        super().describe()
        print(f"  Enforcement:   {self.enforcement}")


# =============================================================================
# PART 2: PROPOSED MODIFIED STAKEHOLDER STRUCTURE
# =============================================================================

class EmpoweredUser(User):
    """
    Proposed: Users gain data portability, revenue participation,
    and a voice in governance.
    """
    def __init__(self, name="Empowered User"):
        super().__init__(name)
        self.data_access = 6      # Can view and export behavioral profile
        self.revenue_share = 3    # Data dividend from ad revenue generated by their data
        self.decision_power = 4   # Participatory governance via user councils
        self.autonomy = self._calc()
        self.can_export_data = True
        self.content_ownership = "N/A (consumer)"

    def describe(self):
        super().describe()
        print(f"  [PROPOSED] Data portability and revenue dividend enabled.")


class EmpoweredCreator(Creator):
    """
    Proposed: Creators receive transparent fixed revenue splits,
    full content ownership, and formal policy representation.
    """
    def __init__(self, name="Empowered Creator"):
        super().__init__(name)
        self.data_access = 7      # Full content performance data
        self.revenue_share = 6    # Fixed percentage of ad revenue from their content
        self.decision_power = 5   # Seat on content policy advisory board
        self.autonomy = self._calc()
        self.content_ownership = "Creator-owned; platform holds non-exclusive license only"
        self.monetization_control = "Transparent fixed-rate split, not at platform's discretion"

    def describe(self):
        super().describe()
        print(f"  [PROPOSED] Fixed revenue split and policy board seat enabled.")


class AccountablePlatform(PlatformOwner):
    """
    Proposed: Platform subject to independent algorithmic audits,
    mandatory data portability, and external governance oversight.
    """
    def __init__(self, name="Accountable Platform"):
        super().__init__(name)
        self.data_access = 8       # Retains operational data; subject to audit
        self.revenue_share = 6     # Reduced as revenue redistributed to users/creators
        self.decision_power = 6    # Constrained by oversight board and portability rules
        self.autonomy = self._calc()
        self.algorithm_transparency = "Mandatory annual independent third-party audit"
        self.content_license = "Non-exclusive license only; creator retains full ownership"
        self.monetization_terms = "Fixed, disclosed revenue split with creators"

    def describe(self):
        super().describe()
        print(f"  [PROPOSED] Algorithm audits and independent governance enabled.")


# =============================================================================
# PART 3: TRANSITION FUNCTIONS
# =============================================================================

def migrate_user_to_empowered(old: User) -> EmpoweredUser:
    new = EmpoweredUser(name=old.name)
    print(f"\n[MIGRATION] User '{old.name}':")
    print(f"  Data Access:    {old.data_access} -> {new.data_access}")
    print(f"  Revenue Share:  {old.revenue_share} -> {new.revenue_share}")
    print(f"  Decision Power: {old.decision_power} -> {new.decision_power}")
    print(f"  Autonomy Score: {old.autonomy} -> {new.autonomy}")
    return new


def migrate_creator_to_empowered(old: Creator) -> EmpoweredCreator:
    new = EmpoweredCreator(name=old.name)
    print(f"\n[MIGRATION] Creator '{old.name}':")
    print(f"  Data Access:    {old.data_access} -> {new.data_access}")
    print(f"  Revenue Share:  {old.revenue_share} -> {new.revenue_share}")
    print(f"  Decision Power: {old.decision_power} -> {new.decision_power}")
    print(f"  Autonomy Score: {old.autonomy} -> {new.autonomy}")
    return new


def migrate_platform_to_accountable(old: PlatformOwner) -> AccountablePlatform:
    new = AccountablePlatform(name=old.name + " (Reformed)")
    print(f"\n[MIGRATION] Platform '{old.name}':")
    print(f"  Data Access:    {old.data_access} -> {new.data_access}")
    print(f"  Revenue Share:  {old.revenue_share} -> {new.revenue_share}")
    print(f"  Decision Power: {old.decision_power} -> {new.decision_power}")
    print(f"  Autonomy Score: {old.autonomy} -> {new.autonomy}")
    return new


# =============================================================================
# PART 4: DEMO
# =============================================================================

if __name__ == "__main__":
    print("=" * 55)
    print("EXISTING TIKTOK STAKEHOLDER STRUCTURE")
    print("=" * 55)
    for s in [User(), Creator(), Influencer(), Advertiser(), PlatformOwner(), Regulator()]:
        s.describe()

    print("\n" + "=" * 55)
    print("MIGRATIONS TO PROPOSED STRUCTURE")
    print("=" * 55)
    new_user = migrate_user_to_empowered(User("Average User"))
    new_creator = migrate_creator_to_empowered(Creator("Mid-tier Creator"))
    new_platform = migrate_platform_to_accountable(PlatformOwner())

    print("\n" + "=" * 55)
    print("PROPOSED STAKEHOLDER STRUCTURE")
    print("=" * 55)
    for s in [new_user, new_creator, Influencer(), Advertiser(), new_platform, Regulator()]:
        s.describe()

    # Summary stats
    existing = [User(), Creator(), Influencer(), Advertiser(), Regulator()]
    proposed = [new_user, new_creator, Influencer(), Advertiser(), Regulator()]
    avg_existing = round(sum(s.autonomy for s in existing) / len(existing), 2)
    avg_proposed = round(sum(s.autonomy for s in proposed) / len(proposed), 2)
    print(f"\n--- Summary ---")
    print(f"Avg autonomy (non-platform, existing):  {avg_existing}/10")
    print(f"Avg autonomy (non-platform, proposed):  {avg_proposed}/10")
    print(f"Platform autonomy (existing):           {PlatformOwner().autonomy}/10")
    print(f"Platform autonomy (proposed):           {new_platform.autonomy}/10")
