def print_scores(**kw):
    print('      Name  Score')
    print('------------------')
    for name, score in kw.items():
        print('%10s  %d' % (name, score))
    print()


print_scores(Adam=99, Lisa=88, Bart=77)
data = {'Adam Lee': 99, 'Lisa S': 88, 'F.Bart': 77}
print_scores(**data)
