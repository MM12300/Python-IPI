def cleanMessage(message,charList):
    for char in charList:
        message = message.replace(char,'')
    return message
    
def compterMots(message):
    message=cleanMessage(message,['.',',','\'','"',';','\n'])
    listeMots=message.lower().split(' ')
    print(listeMots)
    ensembleMots=set(listeMots)
    occurences={}
    for mot in ensembleMots:
        occurences[mot]=listeMots.count(mot)
    return occurences





def main():
    message="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin egestas condimentum sagittis. In tempor, enim porttitor scelerisque cursus, ex dui luctus purus, ut dignissim nisi ipsum ut sapien. Integer quis velit sagittis, commodo massa lacinia, placerat elit. Quisque auctor tristique tortor, id varius odio semper sit amet. Maecenas ultricies turpis ut sagittis gravida. Integer faucibus mollis tempor. Duis sed risus vestibulum, ultrices nisi non, pretium ante. Morbi in lacus vestibulum, molestie neque quis, gravida eros. Quisque quis odio nisi. Etiam porttitor leo nibh, nec volutpat dui tincidunt ac. Maecenas vel semper libero. Donec placerat a libero in aliquam. Fusce gravida auctor dolor, eu hendrerit justo gravida vitae. Maecenas id commodo erat, ac hendrerit ante.
Aliquam eleifend interdum eleifend. Nunc sagittis mauris eget nisl ornare laoreet. Morbi dolor turpis, cursus non quam in, molestie porta diam. Nunc laoreet facilisis nunc, in volutpat arcu lobortis id. Mauris ultricies rutrum tortor ut tincidunt. Nulla vulputate cursus volutpat. Nunc interdum turpis a urna semper suscipit. Mauris enim nunc, hendrerit quis sem et, rhoncus accumsan sem.
In id dui ac neque pretium ultricies eu vitae elit. In sem justo, tincidunt sagittis lectus a, lacinia pellentesque ex. Ut sed congue dolor, ut molestie metus. Nullam commodo commodo semper. Nullam eros arcu, euismod nec pellentesque ullamcorper, commodo ac arcu. Nam vestibulum metus ac velit eleifend iaculis. Duis ornare dui nec lorem dignissim mattis. Sed faucibus ac risus eget vehicula.
Cras ultricies facilisis tortor. Phasellus tempor tincidunt metus dictum lacinia. Nulla facilisi. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Aenean facilisis, ipsum a mollis sollicitudin, odio mauris auctor libero, tincidunt convallis ante arcu quis sapien. Curabitur lobortis dapibus laoreet. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean a turpis id odio porta feugiat. Integer imperdiet sagittis enim eu auctor. Nunc blandit lobortis pellentesque. Sed vel nibh rhoncus, egestas augue eu, volutpat ex. Sed posuere commodo dictum. Nullam risus felis, convallis vel sem eget, pellentesque mollis quam. Maecenas malesuada ipsum vel tellus accumsan vestibulum.
In finibus mollis tempus. Curabitur eget ante varius, faucibus nulla sed, commodo est. Quisque fringilla leo nec imperdiet facilisis. Nullam sit amet massa porta, ultricies neque sed, viverra leo. Pellentesque suscipit diam eget turpis dignissim dapibus. Maecenas sagittis pulvinar augue, sed malesuada odio venenatis eu. Vivamus feugiat quam sed venenatis lobortis. Maecenas sapien eros, ornare pharetra nulla a, congue interdum enim. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    print(compterMots(message))
if __name__=='__main__':
    main()