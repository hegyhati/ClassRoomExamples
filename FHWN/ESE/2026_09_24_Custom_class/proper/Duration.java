public class Duration implements Comparable<Duration>{
    private final int _seconds;

    public Duration(int seconds) {this._seconds = seconds;}

    public int toSeconds() { return _seconds; }
    public Duration divide(double divider) { return new Duration((int) ((double)_seconds/divider)); }

    @Override
    public String toString() {
        final int hours = _seconds / 3600;
        final int minutes = (_seconds / 60) % 60;
        final int seconds = _seconds % 60;

        return hours > 0 
            ? String.format("%d:%02d:%02d", hours, minutes, seconds)
            : String.format("%d:%02d", minutes, seconds)
            ;
    }    

    @Override
    public int compareTo(Duration other) {
        return _seconds - other._seconds;
    }
}