public class Run {

    public enum RunType {
        REGULAR,
        GROUP,
        RACE;

        @Override
        public String toString() {
            return switch (this) {
                case REGULAR -> "regular run";
                case GROUP -> "grouprun";
                case RACE -> "race";
            };
        }
    }

    private final double _distanceInKm;
    private final Duration _duration;
    private final RunType _type;

    public Run(double distance, Duration duration, RunType type) {
        this._distanceInKm = distance;
        this._duration = duration;
        this._type = type;
    }

    @Override
    public String toString() {
        return String.format(
            "Distance: %s km, Time: %s, Average pace: %s. This was a %s.",
            _distanceInKm,
            _duration,
            getPace(),
            _type
        );        
    }

    public double getDistanceInKm() { return _distanceInKm; }
    public Duration getDuration() { return _duration; }
    public RunType getType() { return _type; }
    public Duration getPace() { return _duration.divide(_distanceInKm); }
    
    public boolean isLongerThan(Run other) { return _distanceInKm >= other._distanceInKm; }
    public boolean isFasterThan(Run other) { return getPace().compareTo(other.getPace()) < 0; }
}