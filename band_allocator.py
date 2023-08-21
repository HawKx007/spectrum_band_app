class BandAllocator:
    def __init__(self, start_freq, end_freq, levels):
        self.start_freq = start_freq
        self.end_freq = end_freq
        self.levels = levels
        self.band_width = (end_freq - start_freq) / levels
        self.allocations = [None] * levels
        self.users = [''] * levels  # Add a list to store user names

    def allocate_band(self, freq, user_name):
        index = int((freq - self.start_freq) / self.band_width)
        if 0 <= index < self.levels and not self.allocations[index]:
            self.allocations[index] = freq
            self.users[index] = user_name  # Store user name when allocated
            return True
        return False

    def get_allocations(self):
        return self.allocations, self.users

