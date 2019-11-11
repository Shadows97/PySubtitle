from googletrans import Translator
from webvtt import WebVTT, Caption

fileName = 'Tests/test1.en.vtt'

with open(fileName) as fp:
   vttFr = WebVTT()
   translator = Translator()

   for cnt, line in enumerate(fp):
      if '-->' in line:
          t = line.split('-->')
          print(t.pop())
          print(open(fileName).readlines()[cnt+1])
          recFr = translator.translate(open(fileName).readlines()[cnt+1], dest='fr')
          captionFr = Caption( t[0], t.pop(), recFr.text)
          vttFr.captions.append(captionFr)
          
   vttFr.save('Tests/test1.fr.vtt')