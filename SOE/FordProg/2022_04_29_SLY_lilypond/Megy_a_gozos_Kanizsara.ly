\version "2.12.3"

\header
{
  title = "Megy a gőzös Kanizsára"
  tagline = \markup{"Typeset by Máté Hegyháti using LilyPond"  #(ly:export (lilypond-version))}
}

\paper
{
  #(set-paper-size "b4")

  line-width = #170
  after-title-space = #30
  %annotate-spacing = ##t
  %between-system-padding = #20
  between-system-space = #30
  %ragged-last-bottom = ##f
  %ragged-bottom = ##f
  %%bottom-margin = #0
  %top-margin = #0

}



dal = {
  <<
    \new Voice
    {
      \set midiInstrument = #"violin"
      \time 2/4
      \clef violin
      \key d \major
      \transpose c c'
      {
        \repeat volta 2
        {
          d8 d fis d
          a a b a
          g fis e4
          d r
        }
        \break
        g8 a b4
        b r
        d'8 cis' b4
        a r
        \break
        d'8 a fis d
        a a b a
        g fis e4
        d r
      }
      \bar "|."
    }
    \addlyrics
    {
      Megy a gő -- zös, megy a gő -- zös, Ka -- ni -- zsá -- ra,
      E -- lől áll a ma -- si -- nisz -- ta,
      Ki a gő -- zöst, ki a gő -- zöst i -- ga -- zít -- ja.
    }
    \addlyrics
    {
      Ka -- ni -- zsa -- i, ka -- ni -- zsa -- i ál -- lo -- más -- ra.
    }
  >>
}


\score
{
  \dal

  \layout
  {
    indent = #0
  }
}



\score
{
  \unfoldRepeats{
  \dal
  }
  \midi
  {
    \context
    {
      \Staff
      \remove "Staff_performer"
    }
    \context
    {
      \Voice
      \consists "Staff_performer"
    }
    \context
    {
      \Score
      tempoWholesPerMinute = #(ly:make-moment 96 4)
    }
  }

}

\markup
{
  \fill-line
  {
    \column
    {
      \hspace #0.1
      \line{Megy a gőzös, megy a gőzös, Kanizsára,}
      \line{Kanizsai állomásról Kaposvárra.}
      \line{Rajta ül a bíró lánya,}
      \line{Százfodros a, százfodros a tunikája.}

      \hspace #0.1
      \line{Hallották-e, hallották-e, hogy mi történt,}
      \line{Tegnap este lenyeltem egy villanykötét,}
      \line{Azon vettem magam észre,}
      \line{hátra felé világítok a sötétbe'.}

      \hspace #0.1
      \line{Volt szeretőm, volt szeretőm, tizenhárom,}
      \line{Tíz elhagyott, tíz elhagyott maradt három,}
      \line{Kettő megcsal, maradt még egy,}
      \line{Azt az egyet, azt az egyet én csalom meg.}
    }
  }
}
