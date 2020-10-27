import { mount } from '@vue/test-utils'
import { LangName } from '../../../src/ts/languages'
import Button from '../../../src/components/LangSelect/Button'

describe('Language Selection / Button', () => {
  it('shows the correct language name passed from props', () => {
    const wrapper = mount(Button, {
      props: {
        name: LangName.RUS
      }
    })

    const btn = wrapper.find('button')
    expect(btn.text()).toStrictEqual(LangName.RUS)
  })

  describe('[EVENT] update-menu-visibility', () => {
    it('emits btn on click', async () => {
      const wrapper = mount(Button)
      const btn = wrapper.find('button')
      await btn.trigger('click')

      expect(wrapper.emitted('update-menu-visibility')).toBeTruthy()
    })

    it('returns opposite boolean state of showOptions', async () => {
      const wrapper = mount(Button, {
        props: {
          showOptions: false
        }
      })

      const btn = wrapper.find('button')

      await btn.trigger('click')
      expect(wrapper.emitted('update-menu-visibility')[0]).toEqual([true])

      await wrapper.setProps({
        showOptions: true
      })

      await btn.trigger('click')
      expect(wrapper.emitted('update-menu-visibility')[1]).toEqual([false])
    })
  })
})
